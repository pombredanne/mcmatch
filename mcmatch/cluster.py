'''
Transformation analysis algorithms and support.

@author: niko
'''
from mcmatch.db.types import Codeblock, FnMetric, Fn
from mcmatch.util import extract_funname, NProgressPrinter,\
  signature_to_fname_heuristic
import numpy as np
from sklearn.neighbors import NearestNeighbors, KDTree
from sklearn import preprocessing
from sklearn.decomposition import PCA, RandomizedPCA

from mcmatch.db.database import FunDB
from mcmatch.db.pg_database import PgFunDB
from sklearn.preprocessing.data import StandardScaler
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt
import logging
import sklearn
from sklearn.decomposition.kernel_pca import KernelPCA
from metric_learn import LMNN, NCA
from collections import defaultdict

class LabelTransformer(object):
  """transforms a list of string labels into a numpy array of
  integer (actually, double) labels, and back"""

  def __init__(self, labels):
    """Initialize the transformers with an array of string labels"""
    i = 0
    lbl_map = {}
    lst = []
    for l in labels:
      if l not in lbl_map:
        lbl_map[l] = i
        i += 1
      lst.append(lbl_map[l])

    lbl_map_r = {}
    for k, v in lbl_map.items():
      lbl_map_r[v] = k
    self.lst = lst
    self.i = i

  def int_labels(self):
    """Get the integer representation of the string labels, in the order
    in which they were passed to __init__"""
    return np.array(self.lst, dtype='d')

  def string_label(self, int_label):
    """get the string respresentations of a single label in integer format"""
    return lbl_map_r[int(int_label)]

  def string_labels(self, numpy_labels):
    """return an array of the string representations of an numpy.array or list of labels."""
    ret = []
    for lbl in numpy_labels:
      ret.append(self.string_label(lbl))
    return ret


def filter_trainingset(trainset, labels, k):
    """Filter a trainingset to contain only those instances, whos class (as determined by
    associated labels) appears at least k times.
    
    Returns the filtered trainingset as well as the indices used for filtering (which can then
    be applied to the label data).
    """
    lblctr = defaultdict(int)
    for lbl in labels:
        lblctr[lbl] += 1
    indices = np.array(map(lambda l: lblctr[l] >= k, labels), dtype=bool)
    return trainset[indices], indices

def filter_classes(trainset, trainset_labels, testset_labels):
  """Filter a set of training set instances and their associated labels
  to only contain the classes contained in testset_labels.

  Returns a tuple of the filtered training set and the filtered label list."""
  indices = np.array(map(lambda l: l in testset_labels, trainset_labels), dtype=bool)
  trainset_classes = np.array(trainset_labels)[indices]
  return trainset[indices], trainset_classes


class TransformPipeline(object):
  """A transformation pipeline, similar to scikit-learn's sklearn.pipeline.Pipeline."""
  TRANSFORM_SCALE = 1
  TRANSFORM_PCA = 2
  TRANSFORM_RANDOM_PCA=4
  TRANSFORM_KERNEL_PCA=8
  TRANSFORM_LMNN = 16
  TRANSFORM_NCA = 32
  
  def __init__(self, init_with = 0):
    """Initialize the transformation pipleine, with an optional list of transformation
    modes. init_with can be any bitwise-or'd combination of the TRANSFORM_* modes."""
    self.pipeline = []
    self.supervised_pipeline = []
    self.mink = 4
    
    if init_with & self.TRANSFORM_SCALE:
      self.add_standard_scaler()
    if init_with & self.TRANSFORM_PCA:
      self.add_pca()
    if init_with & self.TRANSFORM_RANDOM_PCA:
      self.add_random_pca()   
    if init_with & self.TRANSFORM_KERNEL_PCA:
      self.add_kernel_pca()
    if init_with & self.TRANSFORM_LMNN:
      self.supervised_pipeline.append(LMNN(k=self.mink))
    if init_with & self.TRANSFORM_NCA:
      self.supervised_pipeline.append(NCA())
   
  def add(self, stage):
    """Add any sklearn.base.TransformerMixin instance to the (unsupervised) pipeline."""
    assert isinstance(stage, sklearn.base.TransformerMixin)
    self.pipeline.add()
    
  def add_pca(self):
    self.pipeline.append(PCA())
  
  def add_random_pca(self):
    self.pipeline.append(RandomizedPCA())
  
  def add_standard_scaler(self):
    self.pipeline.append(StandardScaler())
  
  def add_kernel_pca(self):
    self.pipeline.append(KernelPCA())
  
  def transform_trainingset(self, ts, labels=None):
    """Transform the trainingset by fitting and applying each
    transformer in the pipeline.

    If a supervised method (TRANSFORM_LMNN or TRANSFORM_NCA) is used,
    the labels parameter needs to be set to a list of class labels.
    
    Returns the updated training set.
    """
    for p in self.pipeline:
      ts = p.fit_transform(ts)
    
    if not len (self.supervised_pipeline):
      return ts

    if labels is None and len(self.supervised_pipeline):
      raise RuntimeError("supervised transformer called without labels argument")
    
    print labels
    lblt = LabelTransformer(labels)
    labels = lblt.int_labels()
    print labels
    mink = self.mink
    #filtered_ts, filter_idx = filter_trainingset(ts, labels, mink)
    #filtered_labels = labels[filter_idx]

    for p in self.supervised_pipeline:
      p.fit(ts, labels)
      ts = p.transform(ts)
    
    #self.lblt = lblt
    return ts
  
  def transform_testset(self, ts):
    """Apply the transformations in the pipeline to the
    passed testset and return the transformed result."""
    for p in self.pipeline:
      ts = p.transform(ts)
    
    for p in self.supervised_pipeline:
      ts = p.transform(ts)
    
    return ts
  

class DistanceInfo(object):
  """Class to measure variations in the distance distribution of test instances to training sets
  under various transformations."""
  def __init__(self, db, metric,
               transform=0,
               training_repositories=None, norm="cityblock"):
    assert isinstance(db, FunDB)
    assert isinstance(metric, FnMetric)
    if training_repositories is not None:
      assert isinstance(training_repositories, list)

    self.metric = metric
    if isinstance(transform, TransformPipeline):
      self.transformers = transform
    else:
      self.transformers = TransformPipeline(init_with=transform)
    
    self.training_repositories = training_repositories
    self.norm = norm
    
    self._train(db)
  
  def _train(self, db):
    assert isinstance(db, FunDB)
    self.trainingset_idx_to_ftid, train_data = db.get_metrics_np(self.metric, in_repositories=self.training_repositories, include_signature=True)
    self.known_function_names = map(lambda z: signature_to_fname_heuristic(z[1]), self.trainingset_idx_to_ftid)
    train_data = self.transformers.transform_trainingset(train_data, self.known_function_names)
    self.train_data = train_data

  def has_function(self, function_name):
    
    if function_name in self.trainingset_idx_to_ftid:
      return True
    return False

  def _test(self, test_data):
    """if enabled, scale the test data and
    return the pairwise distances matrix."""
    if not len(test_data):
      raise Exception("Cannot test empty test data set")
      # well, actually, we could just return an empty matrix.
      # but it's probably an error anyway.
    test_data = self.transformers.transform_testset(test_data)
    return pairwise_distances(test_data, self.train_data, metric=self.norm)
    
  def test(self, db, in_repositories=None):
    """returns a tuple:
    (pairwise distance as numpy matrix, testset_functiontext_info)"""
    assert isinstance(db, FunDB)
    logging.info("Retrieving metrics for test set")
    testset_idx_to_ftid, test_data = db.get_metrics_np(self.metric, in_repositories=in_repositories, include_signature=True)
    if not len(testset_idx_to_ftid):
      raise Exception("no metrics returned!")
    logging.info("Calculating pairwise distances")
    self.test_data = test_data
    return (self._test(test_data), testset_idx_to_ftid)

  def test_codeblock(self, cb):
    assert isinstance(cb, Codeblock)
    self.metric.calculate(cb)
    test_data = np.array([self.metric.get_sql_contents()])
    if isinstance(cb, Fn):
      assert isinstance(cb, Fn) # for pydev.
      testset_info = (-1, cb.sig)
    else:
      testset_info = (-1, "codeblock")
    
    return self._test(test_data), [testset_info]
  
  
  def get_trainingset_infos(self):
    """returns a vector that maps from the test data at each idx (typically column)
    to the corresponding function text info tuple (function_text_id [, signature])"""
    return self.trainingset_idx_to_ftid
  
  @staticmethod
  def make_equivalence_map(testset_infos, trainingset_infos, key=lambda x: extract_funname(x[1])):
    """returns a mapping from each index in the testset to the equivalent functions in the training set."""
    ti_reverse = {}
    for ti, tt in enumerate(trainingset_infos):
      k = key(tt)
      if k not in ti_reverse:
        ti_reverse[k] = [ti]
      else:
        ti_reverse[k].append(ti)
    result = []
    for te in testset_infos:
      k = key(te)
      if k not in ti_reverse:
        result.append([])
      else:
        result.append(ti_reverse[k])
    return result
  
  def print_infos(self, pairwise_d, testset_info):
    assert isinstance(pairwise_d, np.ndarray)
    
    col_ftids = self.get_trainingset_infos()
    row_ftids = testset_info
    
    col_extracted_funnames = [extract_funname(f[1]) for f in col_ftids]
    logging.info("Looking up matching functions")
    
    pp = NProgressPrinter(len(row_ftids))
    
    # statistics
    n_matching_rows = 0
    n_matches_in_matching_rows = 0
    
    
    for ftid_i in range(0, len(row_ftids)):
      pp.bump()
      ftid = row_ftids[ftid_i]
      ft_funname = extract_funname(ftid[1])
      
      this_row_matches = 0
      
      print ft_funname, " mean=", np.mean(pairwise_d[ftid_i]), " stddev=", np.std(pairwise_d[ftid_i]), " d=[",
      for cftid_i in range(0, len(col_ftids)):
        if ft_funname == col_extracted_funnames[cftid_i]:
          this_row_matches += 1
          print ' dist=', pairwise_d[ftid_i][cftid_i], " id=", cftid_i, ",",
      print "]"
      
      if this_row_matches > 0:
        n_matching_rows += 1
        n_matches_in_matching_rows += this_row_matches
  
    print "identical function names (hits): %d of %d (%4f%%)." % (n_matching_rows, len(row_ftids), n_matching_rows*100.0/len(row_ftids))
    print "on hit, avg num matches: %f" % (n_matches_in_matching_rows/float(n_matching_rows))
  
  @staticmethod
  def make_graph_single(distances_single, testset_tuple, equivalences, valueRange=None, equiNames=None,
                        train_name="training", test_name="test"):
    if valueRange is None:
      valueRange = (0, 30) 
    plt.hist(distances_single, bins=100, range=valueRange, label="distance histogram")
    funname = testset_tuple[1]
    try:
      funname = extract_funname(testset_tuple[1])
    except ValueError:
      pass
    
    plt.xlabel("distance from %s (%s)" % (funname, test_name))
    plt.ylabel("number of functions")
  
    equi_funnames = []
    color_rot = ['r', 'g', 'c', 'm', 'y']
    color_rot_idx = 0
    for i, equi_idx in enumerate(equivalences):
      if i >= len(equiNames):
        equi_funnames.append("?")
      try:
        equi_funnname = extract_funname(equiNames[i])
      except:
        equi_funnname = equiNames[i]
      equi_funnames.append(equi_funnname + " (%s)" % (train_name))
      plt.axvline(distances_single[equi_idx], label=equi_funnname, color=color_rot[color_rot_idx])
      color_rot_idx = (color_rot_idx + 1) % len(color_rot)
    plt.legend(list(reversed(['all (%s)' % (train_name)] + list(reversed(equi_funnames)))))

  @staticmethod
  def get_partition_sizes(distances_single, testset_tuple, equivalences):
    """returns n (=len(equivalences)) tuples, each describing
     (n_lower, n_equal, n_larger) - the amount of lower, equal and larger
     distacens in distances_single, in relation to the elements at the
     indizes in equivalences."""
    if not len(equivalences):
      return []
    distances = map(lambda z: distances_single[z], equivalences)
    partitions = [(0,0,0)]*len(distances)
    
    for d in distances_single:
      for distidx, dist in enumerate(distances):
        p = partitions[distidx]
        if d < dist:
          partitions[distidx] = (p[0]+1, p[1], p[2])
        elif d == dist:
          partitions[distidx] = (p[0], p[1]+1, p[2])
        elif d > dist:
          partitions[distidx] = (p[0], p[1], p[2]+1)
    return partitions
  
  def make_graphs(self, pairwise_d, testset_infos, equivalence_map):
    for row_idx, testset_tuple in enumerate(testset_infos):
      if row_idx < 100:
        continue
      row_funname = extract_funname(testset_tuple[1])
      print row_idx, row_funname
      self.make_graph_single(pairwise_d[row_idx], testset_tuple, equivalence_map[row_idx])
      if row_idx > 200:
        break
  

  @staticmethod
  def lowest_matching(pairwise_d, testset_infos, equivalence_map, do=lambda test_idx, train_idx, dist: dist):
    results = []
    for row_idx, row_info in enumerate(testset_infos):
      lowest_matching_idx = None
      lowest_match_dist = None
      for equi_idx in equivalence_map[row_idx]:
        if lowest_matching_idx is None or lowest_match_dist < pairwise_d[row_idx][equi_idx]:
          lowest_matching_idx = equi_idx
          lowest_match_dist = pairwise_d[row_idx][equi_idx]

      if lowest_matching_idx is None:
        results.append(None)
      else:
        results.append(do(row_idx, equi_idx, lowest_match_dist))
    return results
  
  def testAB(self, pairwise_d, testset_infos, equivalence_map=None):
    if equivalence_map is None:
      equivalence_map = self.make_equivalence_map(testset_infos, self.get_trainingset_infos())
    good, bad, other = 0, 0, 0
    for i in range(0, len(equivalence_map)):
        res = DistanceInfo.get_partition_sizes(pairwise_d[i], None, equivalence_map[i])
        for el in res:
            if el[0] < el[2]:
                good += 1
            elif el[0] > el[2]:
                bad += 1
            else:
              other += 1
    return good, bad, other
  
  @staticmethod
  def make_aggregate_hists(pairwise_d, testset_infos, equivalence_map, bins=30, range=(0,30)):
    hist, bins = np.histogram(pairwise_d, bins=bins, range=range)
    closest_dists = DistanceInfo.lowest_matching(pairwise_d, testset_infos, equivalence_map)
    closest_dists = filter(lambda z: z is not None, closest_dists)
    cdhist, cdbins = np.histogram(closest_dists, bins=bins, range=range)
    return bins, hist, cdhist
  
  @staticmethod
  def make_aggregate_graph(pairwise_d, testset_infos, equivalence_map, title=None,
                           train_name="training", test_name="test"):
    bins, hist, cdhist = DistanceInfo.make_aggregate_hists(pairwise_d, testset_infos, equivalence_map)
    fig, ax1 = plt.subplots()
    allf, = ax1.plot(bins[1:], hist, label="all (%s)" % train_name)
    ax1.set_xlabel("distance (from %s)" % test_name)
    ax1.set_ylabel("number of functions")
    ax2 = ax1.twinx()
    ax2.set_ylabel("number of equivalences")
    equi, = ax2.plot(bins[1:], cdhist, color='r', alpha=0.7, label="equivalence positions")
    plt.legend(handles=[allf, equi])
    if title is not None:
      plt.title(title)
    return fig
  
  
class KNearestNeighbors(object):
  def __init__(self, db, metric, k=30, transform=0, training_repositories=None, norm='euclidean'):
    """Initialize the K-Nearest-Neighbours clusterers.
    This will immediately query the database and store the
    results within this instance, make sure to get rid of the
    object after use ASAP."""
    assert isinstance(db, FunDB)
    assert isinstance(metric, FnMetric)
    self.nn = None
    self.fids = []
    self.features = metric
    self.norm = norm
    
    if isinstance(transform, TransformPipeline):
      self.transformers = transform
    else:
      self.transformers = TransformPipeline(init_with=transform)
    
    self.filter_in_repositories = training_repositories
    self._train(db, k)

  def _train(self, db, k):
    assert isinstance(db, PgFunDB)
    self.fids, fdata = db.get_metrics_np(self.features, in_repositories=self.filter_in_repositories)
    self.training_function_names = map(lambda z: signature_to_fname_heuristic(z[1]), self.fids)
    self.transformers.transform_trainingset(fdata, self.training_function_names)
    if self.norm == 'cosine':
      algo = 'brute'
    else:
      algo = 'auto'
    self.nn = NearestNeighbors(n_neighbors=k, algorithm=algo, metric=self.norm).fit(fdata)

  def _convert_indizes(self, indizes):
    """convert indizes (row index in the training dataset) to the associated
    function id. Return value is a list of lists."""
    return [[self.fids[idx] for idx in indizes[k]] for k in range(0, indizes.shape[0])]


  def get_neighbours(self, codeblock):
    """returns a tuple (
      distances -- a numpy matrix with one row, each column containing the distances
      fn_text_ids -- a numpy array containing, at index i, the function_text id belonging to distance i.
      )"""
    assert isinstance(codeblock, Codeblock)
    self.features.calculate(codeblock)
    print self.features.get_sql_columns()
    print self.features.get_sql_contents()

    codeblock_metric = np.array(self.features.get_sql_contents())
    self.transformers.transform_testset(codeblock_metric)
    distances, ft_info = self.nn.kneighbors(codeblock_metric)
    fn_text_ids = [self.fids[idx] for idx in ft_info[0]]
    return distances, fn_text_ids

  def get_neighbours_of_functions(self, db, in_repositories=None):
    """performs a full k-nearest-neighbours search on a set of functions from the database, filtered
    by the optional parameter (singular, hopefully plural in the future).

    Returns a tuple: (fids, distances, distance_to_id).
    distances and indizes are numpy arrays, fn_text_ids is a list of lists.

    - fids: the function ids associated with each row
    - distances, distance_to_id: two matrices of the same dimensions. Each row i describes the nearest
      k functions (distance in distances, function id in distance_to_id) to the function(id) given
      in fids at index i.
    """
    #codeblock_metrics = np.
    test_info, test_data = db.get_metrics_np(self.features, in_repositories=in_repositories)
    test_data = self.transformers.transform_testset(test_data)
    distances, indizes = self.nn.kneighbors(test_data)

    train_info = self._convert_indizes(indizes)
    return test_info, distances, train_info

  def test(self, fdb, in_repositories):
    return self.get_neighbours_of_functions(fdb, in_repositories)
  
  def has_function(self, function_name):
    if function_name in self.training_function_names:
      return True
    return False
