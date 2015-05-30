#!/usr/bin/python2
from mcmatch.db.types import ObjectInfo, FnDiff
from mcmatch.db.pg_database import PgFunDB as DB
from mcmatch.cluster import KNearestNeighbors, DistanceInfo
from mcmatch.commandline import FeatureArg
from mcmatch.util import extract_funname, NProgressPrinter
import logging
import re
import sys
import argparse
from collections import defaultdict
import mcmatch



def do_knn(fdb, aggr, scale_features, repo_a, repo_b):
  knn = KNearestNeighbors(fdb, aggr, k=50, scale_features=scale_features, filter_in_repositories=repo_a)
  row_function_info, distances, repo_a_indexmapping = knn.get_neighbours_of_functions(db=fdb, in_repositories=[repo_b])

  dist_sum = 0
  match_count = 0
  
  for i in range(0, len(row_function_info)):
    root_funname = extract_funname(row_function_info[i][1])
    for j in range(0, len(distances[i])):
      dst = distances[i][j]
      col_function_info = repo_a_indexmapping[i][j]
      fname = extract_funname(col_function_info[1])
      if fname == root_funname:
        print "-> %3d %8f %s" % (j, dst, fname)
        dist_sum += j
        match_count += 1
  
  print "found in 50-nearest: %d of %d. Avg-k: %4f" % (match_count, len(row_function_info), float(dist_sum)/match_count)

def do_dist(fdb, aggr, scale_features, train_sets, test_set):
  di = DistanceInfo(fdb, aggr, training_repositories=train_sets)
  pairwise_d, testset_info = di.test(fdb, test_set)
  di.print_infos(pairwise_d, testset_info)

def main():
  logging.basicConfig(level=logging.DEBUG)
  parser = argparse.ArgumentParser(description='perform diff actions between functions in the database')
  parser.add_argument('-a', '--repository-a', dest='training_sets', default=[], action="append",
      help='compare given function to all others (filters apply). Can be specified multiple times.')
  parser.add_argument('-b', '--repository-b', dest='test_set', default=None,
      help='only process functions in objects whose name contains this parameter. Can be specified multiple times to match name against any of the list.')
  parser.add_argument('-l', '--list', dest='list',
      action='store_true',
      help='list repositories',
      default=None)

  parser.add_argument('-f', '--list-functions', dest='list_functions_in',
      help='list functions in given repository',
      default=None)
  FeatureArg.apply(parser)
  args = parser.parse_args()


  fdb = DB()
  if args.list:
    i = 0
    for repo in fdb.get_repository_names():
      print repo
      i += 1
    print "%d repositories." % i
    return

  if args.list_functions_in:
    i = 0
    for fun in fdb.get_functions_by_repository(args.list_functions_in):
      print fun.get_shortinfo(db=fdb)
      i += 1
    print "%d functions in %s." % (i, args.list_functions_in)
    return

  if not len(args.training_sets)  or args.test_set is None:
    logging.error("ERROR: Either -l, -f or both -a and -b are required.")
    return

  functions_a = list(fdb.get_function_texts_by_repository(args.training_sets))
  functions_b = list(fdb.get_function_texts_by_repository(args.test_set))

  logging.info("repository %s: %d functions" % (args.training_sets, len(functions_a)))
  logging.info("repository %s: %d functions" % (args.test_set, len(functions_b)))

  if not len(functions_a):
    logging.error("repository %s has no functions" % (args.training_sets))
    return

  if not len(functions_b):
    logging.error("repository %s has no functions" % (args.test_set))
    return

  aggr = FeatureArg.get_aggregator(args)
  scale_features = FeatureArg.scale_features(args)

  do_knn(fdb, aggr, scale_features, args.training_sets, args.test_set)
  do_dist(fdb, aggr, scale_features, args.training_sets, args.test_set)

if __name__ == "__main__":
  main()
