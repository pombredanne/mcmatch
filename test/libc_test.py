'''
Created on Jan 29, 2015

@author: niko
'''
import sys, os

MCMATCH_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

sys.path.append(MCMATCH_BASE)

# there is a weird bug *SOMEWHERE* when importing mcmatch.cluster.
# Importing NeaerestNeighbors and KDTree first seems to fix that.
from sklearn.neighbors import NearestNeighbors, KDTree
import unittest
import testing.postgresql
import psycopg2
from mcmatch.db.types import Fn, ObjectInfo, Codeblock
from mcmatch.db.pg_database import PgFunDB
from mcmatch.db.compileroptions import CompilerOptions
from mcmatch.extraction import process_dir, process_file
from mcmatch.metric.aggregator import MetricAggregator
from mcmatch.metric.counter import counter_metrics
from mcmatch import cluster
import logging

class Test(unittest.TestCase):
  def setUp(self):
    sql_init_bare_fname = os.path.join(MCMATCH_BASE, "sql/init_bare.psql")

    logging.info("setting up database")
    self.postgresql = testing.postgresql.Postgresql()
    self.conn = psycopg2.connect(**self.postgresql.dsn())
    with self.conn.cursor() as cursor:
      cursor.execute(open(sql_init_bare_fname, "r").read())
    self.fdb = PgFunDB(conn=self.conn)

    logging.info("extracting functions")
    glibc = os.path.join(MCMATCH_BASE, "test/libc_data/libc-2.20.so")
    process_file(self.fdb, glibc, False, True)
    obj = self.fdb.get_object(self.fdb.get_objectids_matching(filename_is="libc-2.20.so")[0])
    obj.get_compileopts().set_repository("glibc-2.20")
    self.fdb.set_compiler_options(obj)

    dietlibc = os.path.join(MCMATCH_BASE, "test/libc_data/dietlibc/libc.so")
    process_file(self.fdb, dietlibc)
    objids = self.fdb.get_objectids_matching(path_contains="test/libc_data/dietlibc/")
    for objid in objids:
      obj = self.fdb.get_object(objid)
      obj.get_compileopts().set_repository("dietlibc-0.33")
      self.fdb.set_compiler_options(obj)

    logging.info("creating metrics")

    metric_instances = [counter_metrics[m] for m in counter_metrics]
    for m in metric_instances:
      self.fdb.recreate_metrics_table(m)

    function_texts = self.fdb.get_function_texts(with_missing_metrics=metric_instances)

    for row in function_texts:
      text_id, signature, text = row

      c = Codeblock()
      c.disassembly_from_text(text)

      for m in counter_metrics:
        mcounter = counter_metrics[m]
        mcounter.calculate(c)
        self.fdb.store_metrics(text_id, mcounter)
    self.fdb.save()

  def tearDown(self):
    self.conn.close()
    self.postgresql.stop()

  def testRepoDB(self):
    self.assertEqual(1, len(self.fdb.get_objectids_matching(repository_is="dietlibc-0.33")))
    self.assertEqual(1, len(self.fdb.get_objectids_matching(repository_is="glibc-2.20")))
    self.assertEqual(640, len(list(self.fdb.get_functions_by_repository("dietlibc-0.33"))))
    self.assertEqual(2468, len(list(self.fdb.get_functions_by_repository("glibc-2.20"))))

  def testAB(self):
    all_metrics = MetricAggregator([counter_metrics[c] for c in counter_metrics])
    di = cluster.DistanceInfo(self.fdb, all_metrics, training_repositories=['glibc-2.20'], )
    pairwise_d, testset_infos = di.test(self.fdb, in_repositories=['dietlibc-0.33'])
    training_infos = di.get_trainingset_infos()
    em = cluster.DistanceInfo.make_equivalence_map(testset_infos, training_infos)
    good, bad, other = 0, 0, 0
    for i in range(0, len(em)):
        res = cluster.DistanceInfo.get_partition_sizes(pairwise_d[i], None, em[i])
        for el in res:
            if el[0] < el[2]:
                good += 1
            elif el[0] > el[2]:
                bad += 1
            else:
              other += 1
    self.assertEqual(101, good)
    self.assertEqual(69, bad)
    print other

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
