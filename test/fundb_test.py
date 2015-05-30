'''
Created on Jan 29, 2015

@author: niko
'''
import sys, os
MCMATCH_BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

sys.path.append(MCMATCH_BASE)

import unittest
import testing.postgresql
import psycopg2
import time
from mcmatch.db.types import Fn, ObjectInfo
from mcmatch.db.pg_database import PgFunDB
from mcmatch.db.compileroptions import CompilerOptions

class Test(unittest.TestCase):
  def setUp(self):
    sql_init_bare_fname = os.path.join(MCMATCH_BASE, "sql/init_bare.psql")
    
    self.postgresql = testing.postgresql.Postgresql()
    self.conn = psycopg2.connect(**self.postgresql.dsn())
    with self.conn.cursor() as cursor:
      cursor.execute(open(sql_init_bare_fname, "r").read())
    self.fdb = PgFunDB(conn=self.conn)

  def tearDown(self):
    self.conn.close()
    self.postgresql.stop()

  def testEmptyDB(self):
    self.assertEqual(0, len(list(self.fdb.all_functions(False))))
    self.assertEqual(0, len(list(self.fdb.all_functions(True))))
    self.assertEqual(None, self.fdb.get_function_by_id(1, True))
    self.assertEqual(0, self.fdb.get_function_count())
    self.assertEqual(0, len(list(self.fdb.get_repository_names())))
    self.assertEqual([], self.fdb.get_objects([1]))
  
  def testOneObject(self):
    fn = Fn("test", "void test(int x);", "test.c", )
    obj = ObjectInfo("/tmp/test.o", time.time(), [fn], False, None)
    obj.set_compileopts(CompilerOptions.from_string("gcc -O2"))
    self.fdb.store_object(obj)
    self.fdb.save()
    
    # Test valid matchers
    fids = self.fdb.get_objectids_matching(filename_is="test.o")
    self.assertEqual(fids, [1])
    
    fids = self.fdb.get_objectids_matching(filename_contains="test")
    self.assertEqual(fids, [1])
    
    fids = self.fdb.get_objectids_matching(path_contains="mp/")
    self.assertEqual(fids, [1])

    fids = self.fdb.get_objectids_matching(path_contains="mp", filename_contains="test", filename_is="test.o")
    self.assertEqual(fids, [1])
    
    # Test invalid combinations
    fids = self.fdb.get_objectids_matching(path_contains="xp")
    self.assertEqual(fids, [])
    
    fids = self.fdb.get_objectids_matching(path_contains="mp", filename_contains="test", filename_is="test")
    self.assertEqual(fids, [])
    
    obj = self.fdb.get_object(1)
    self.assertEquals(obj.get_path(), "/tmp/test.o")
    self.assertEquals(obj.get_compileopts().get_optlevel(), "2")
    self.assertEquals(obj.get_compileopts().get_compiler(), "gcc")
  
    self.assertEqual(1, len(list(self.fdb.all_functions(False))))
    fun = self.fdb.get_function_by_id(1, False)
    self.assertEqual(1, fun.get_container_object_id())
        
  def testTwoObjects(self):
    fn = Fn("test", "void test(int x);", "test.c", )
    obj = ObjectInfo("/tmp/test.o", time.time(), [fn], False, None)
    obj.set_compileopts(CompilerOptions.from_string("gcc -O2"))
    self.fdb.store_object(obj)
    self.fdb.save()
    
    fn2 = Fn("test2", "void test2(int x);", "test2.c")
    fn3 = Fn("test", "void test(int x);", "test.c")
    
    obj = ObjectInfo("/tmp/test2.o", time.time(), [fn2, fn3], False, None)
    co2 = CompilerOptions()
    co2.set_compiler("gcc")
    co2.set_optlevel("1")
    co2.set_repository("test2")
    obj.set_compileopts(co2)
    self.fdb.store_object(obj)
    # don't save this one - functions should be visible
    # even without fdb.save()
    self.assertEqual(3, self.fdb.get_function_count())
    self.assertEqual(1, self.fdb.get_functions_by_shortname(['test/O2'], False))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
