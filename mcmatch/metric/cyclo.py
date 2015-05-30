'''
Created on Apr 1, 2015

@author: niko
'''
from mcmatch.db.types import FnMetric, Codeblock, DisassemblyLine
from scipy import mean, std

class PseudoCyclometricComplexityMetric(FnMetric):
    columns_tpl = ['jumps_mean', 'jumps_stddev', 'jumps_mean_rel', 'jumps_stddev_rel']

    def __init__(self):
      self.num_cond_jumps = 0
      self.cond_jump_distances = []
      self.columns = ['mn_num_cond_jumps', 'mn_num_cond_jumps_rel']
      for k in ['cond', 'uncond', 'all']:
        self.columns += ['mn_%s_%s' % (k, x) for x in self.columns_tpl]
    
    def _get_dict(self, distances, n_total):
      if not len(distances):
        _mean, _stddev, _mean_rel, _stddev_rel = 0,0,0,0
      else:
        print distances, std(distances)
        _mean = mean(distances)
        _stddev = std(distances)
        _mean_rel = _mean*1.0/n_total
        _stddev_rel = _stddev*1.0/n_total
      return [_mean, _stddev, _mean_rel, _stddev_rel]

    def calculate(self, fn):
      assert isinstance(fn, Codeblock)
      self.num_cond_jumps = 0
      self.cond_jump_distances = []
      self.uncond_jump_distances = []
      self.all_jump_distances = []
      self.num_cond_jumps_rel = 0.0
      self.cond_jump_dst_mean = 0.0
      self.cond_jump_dst_stddev = 0.0
      
      for line in fn.disassembly:
        l = DisassemblyLine()
        l.from_line(line)
        if l.is_conditional_jump():
          self.cond_jump_distances.append(1.0*abs(l.get_jump_offset(False)))
        if l.is_unconditional_jump():
          self.uncond_jump_distances.append(1.0*abs(l.get_jump_offset(False)))
        if l.is_jump():
          self.all_jump_distances.append(1.0*abs(l.get_jump_offset(False)))
      
      self.num_cond_jumps = len(self.cond_jump_distances)
      self.num_cond_jumps_rel = self.num_cond_jumps * 1.0 / len(fn.disassembly)

      _get_dict = lambda z: self._get_dict(z, fn.disassembly_nlines)
      self.data = [self.num_cond_jumps, self.num_cond_jumps_rel] + _get_dict(self.cond_jump_distances) + _get_dict(self.uncond_jump_distances) + _get_dict(self.all_jump_distances)
    
    def get_sql_table(self):
      return "metric_cyclo"
    
    def get_sql_columns(self, fq_select=True, fq_rename=False):
      return self._sql_prep_cols(self.columns, self.get_sql_table(), fq_select, fq_rename)

    def get_sql_contents(self):
      return self.data
    
    def create_table_ddl(self):
      dtypes = ['integer'] + ['float']*(len(self.columns)-1)
      return "\n    " + ",\n    ".join(["%s %s" % t for t in zip(self.columns, dtypes)])
    
    def get_kv(self):
      return dict(zip(self.columns, self.get_sql_contents()))

cyclo_metric = {
  'cyclo': PseudoCyclometricComplexityMetric()
}
