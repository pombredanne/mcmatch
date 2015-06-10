'''
Created on Jan 20, 2015

@author: niko
'''
import unittest
from mcmatch.feature.counter import CallCounter, MultiMnemonicCounterFeature


class CallCounterTest(unittest.TestCase):

    def testCallCounter(self):
        cc = CallCounter()
        self._generic_precheck(cc, False)
        cc.calculate_from_histogram({'add': 3, 'call': 5})
        kv = cc.get_kv()
        self.assertEqual(kv['call'], 5)
        self.assertNotIn('add', kv)
        self.assertSequenceEqual(cc.get_sql_contents(), [5])
        self.assertEqual(cc.get_sql_table(), 'feature_mncounter_call')
        
        sql_chunk_start = "SELECT function_text_id"
        sql_chunk_signature = ", function_text.signature"
        sql_chunk_features = ", feature_mncounter_call.mn_call FROM feature_mncounter_call"
        sql_chunk_ft_join = " JOIN function_text ON function_text_id = function_text.id "
        sql_chunk_repo = "WHERE function_text_id IN ( SELECT functions.function_text_id FROM objects JOIN functions ON functions.objectid = objects.id WHERE objects.repository = ANY(%s))"
        
        standard_sql_select = cc.get_sql_select(None, False)
        self.assertEqual(standard_sql_select[0], sql_chunk_start + sql_chunk_features)
        self.assertEqual(len(standard_sql_select[1]), 0)
        
        sql_select_with_signature = cc.get_sql_select(None, True)
        self.assertEqual(sql_select_with_signature[0], sql_chunk_start + sql_chunk_signature + sql_chunk_features + sql_chunk_ft_join)
        self.assertEqual(len(sql_select_with_signature[1]), 0)
        
        sql_select_in_repositories = cc.get_sql_select(['a', 'b'], True)
        sql_select_in_repositories_simplewhitespace = ' '.join(sql_select_in_repositories[0].strip().split())
        self.assertEqual(sql_select_in_repositories_simplewhitespace,
                         sql_chunk_start + sql_chunk_signature + sql_chunk_features + sql_chunk_ft_join + sql_chunk_repo)

    def _generic_precheck(self, cc, is_relative=False):
      self.assertEqual(len(cc.get_sql_contents()), len(cc.get_sql_columns()))
      self.assertEqual(len(cc.get_sql_contents()), cc.num_features())
      self.assertEqual(cc.get_sql_contents(), [None for x in range(cc.num_features())])
      
      columns = cc.get_sql_columns(False, False)
      for c in columns:
        self.assertIsInstance(c, str)
        self.assertNotIn('.', c)
        self.assertTrue(c.startswith("mn_"))
        if not is_relative:
          self.assertFalse(c.endswith("_rel"))
        else:
          self.assertTrue(c.endswith("_rel"))
        
    def testMultiMnemonicCounter(self):
      cc = MultiMnemonicCounterFeature()
      self._generic_precheck(cc, False)
      
      cc.calculate_from_histogram({'add': 5, 'div': 10})
      v = cc.get_kv()
      self.assertIn('div', v)
      self.assertNotIn('add', v)
      self.assertEqual(v['div'], 10)
      
      self.assertEqual(len(cc.get_sql_contents()), len(cc.get_sql_columns(False, False)))
      self.assertNotIn(None, cc.get_sql_contents())
      self.assertEqual(sum(cc.get_sql_contents()), 10)
      
    def testMultiMnemonicCounterRelative(self):
      cc = MultiMnemonicCounterFeature(relative=True)
      self._generic_precheck(cc, True)
      
      cc.calculate_from_histogram({'add': 5, 'div': 10})
      v = cc.get_kv()
      self.assertIn('div', v)
      self.assertNotIn('add', v)
      self.assertAlmostEqual(v['div'], 10/15.0)
      
      self.assertEqual(len(cc.get_sql_contents()), len(cc.get_sql_columns(False, False)))
      self.assertNotIn(None, cc.get_sql_contents())
      self.assertEqual(sum(cc.get_sql_contents()), 10/15.0)
      

      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
