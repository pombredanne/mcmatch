'''
Created on Feb 19, 2015

@author: niko
'''

from mcmatch.db.types import FnFeature, Codeblock


class TextLengthFeature(FnFeature):
  l = 0
  
  def calculate(self, fn):
    assert isinstance(fn, Codeblock)
    self.l = fn.disassembly_nlines
  
  def get_kv(self):
    return {'textlength' : self.l}
  
  def get_sql_columns(self, fq_select=True, fq_rename=False):
    return self._sql_prep_cols(['textlength'], self.get_sql_table(), fq_select, fq_rename)
  
  def get_sql_contents(self):
    return [self.l]
  
  def get_sql_table(self):
    return 'textlength_feature'
  
  def create_table_ddl(self):
    return " textlength integer "

textlength_features = { 'textlength' : TextLengthFeature() }