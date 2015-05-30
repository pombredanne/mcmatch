'''
Created on Jan 6, 2015

@author: niko
'''

from mcmatch.db.types import FnMetric

class MetricAggregator(FnMetric):
  def __init__(self, metrics):
    self.metrics = metrics
    
  def get_kv(self):
    """Return a key/value pair describing this metric."""
    ret = []
    for mt in self.metrics:
      ret.extend(zip(mt.get_sql_columns(), mt.get_sql_contents()))
    return dict(ret)
  
  def get_sql_table(self):
    return None
  
  def get_sql_columns(self, fq_select=True, fq_rename=True):
    if not fq_select:
      raise Exception("MetricAggregator.get_sql_columns() called with fq_select=False")
    ret = []
    for mt in self.metrics:
      ret.extend(mt.get_sql_columns(True, fq_rename))
    return ret
  
  def get_sql_contents(self):
    ret = []
    for mt in self.metrics:
      ret.extend(mt.get_sql_contents())
    return ret

  def calculate(self, fn):
    for mt in self.metrics:
      mt.calculate(fn)
    return None

  def create_table_ddl(self):
    return ",\n  ".join([x.create_table_ddl() for x in self.metrics])

  def create_view_ddl(self):
    all_elems = []
    for x in self.metrics:
      all_elems.extend(x.get_sql_columns())
    return ",\n  ".join(all_elems)


  def get_sql_select(self, in_repositories=None, include_signature=False):
    if len(self.metrics) == 0:
      raise Exception("Tried to create empty SELECT")

    fields = []
    first_tbl_key = self.metrics[0].get_sql_table() + ".function_text_id"
    
    data_offset = 1 # at which offset in the result row do the actual metrics start?
    
    fields.append(first_tbl_key)
    if include_signature:
      data_offset += 1
      fields.append('function_text.signature')

    for m in self.metrics:
      fields.extend(m.get_sql_columns(fq_rename=True))
    field_list = ", ".join(fields)
    stmt = "SELECT " + field_list + " FROM " + self.metrics[0].get_sql_table()
    for m in self.metrics[1:]:
      stmt += " JOIN " + m.get_sql_table() + " ON " + m.get_sql_table()+".function_text_id = " + first_tbl_key
    if include_signature:
      stmt += " JOIN function_text ON function_text.id = " + first_tbl_key

    t, i = self._sql_select_apply_filter(function_text_id=first_tbl_key, in_repositories=in_repositories)
    stmt  += t
    return stmt, i, data_offset
