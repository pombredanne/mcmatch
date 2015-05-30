from mcmatch.db.types import FnMetric, Fn, Codeblock
'''
Created on Dec 21, 2014

@author: niko
'''

class MultiMnemonicCounterMetric(FnMetric):
  """Instruction Mnemonic Counter. Does not take operand types into account.
  A comparison of instructions by execution time/latency can be found
  in http://www.agner.org/optimize/instruction_tables.pdf
  """
  # a couple of more-expensive operations taken from the agner's instruction
  # list. Excluded are control-flow operations.
  default_mnemonics = [
      # x87 floating point instructions
      'fsqrt', # quite fast, but with long-ish dep chain
      'fsin', 'fcos', 'fsincos', 'fptan', 'fpatan',
      # obscure, rarely used x86 integer operations
      #'aam', 'das', 'daa',
      # less obscure ones: (note, op time depends quite a lot on operand types
      'div', 'idiv',
      # logic:
      'bsr', 'bsf',
      # other
      'sti', 'cpuid',
      # MMX instructions
      'divss', 'divps', 'sqrtss', 'sqrtps']

  def __init__(self, mnemonics=None):
    self.table = {}
    self.mnemonics = mnemonics

  def _get_mnemonics(self):
    if self.mnemonics is not None:
      return self.mnemonics
    else:
      return self.default_mnemonics

  def calculate_from_histogram(self, histogram):
    mnemonics = self._get_mnemonics()
    for mnemonic in mnemonics:
      if mnemonic in histogram:
        self.table[mnemonic] = histogram[mnemonic]
      else:
        self.table[mnemonic] = 0

  def calculate(self, fn):
    assert isinstance(fn, Codeblock)
    self.calculate_from_histogram(fn.get_mnemonic_histogram())

  def get_sql_columns(self, fq_select=True, fq_rename=False):
    mnemonics = self._get_mnemonics()
    columns = ["mn_%s" % x for x in mnemonics]
    if fq_select or fq_rename:
      sqltable = self.get_sql_table()
      if fq_select:
        columns = [sqltable + "." + c for c in columns]
      if fq_rename:
        columns = [c + " AS " + c.replace('.', '_') for c in columns]
    return columns

  def get_sql_contents(self):
    mnemonics = self._get_mnemonics()
    if len(self.table):
      return [self.table[x] for x in mnemonics]
    return [None]*len(mnemonics)

  def get_sql_table(self):
    return "mnemonic_counter_metric"

  def create_table_ddl(self):
    return "  " + ",\n  ".join(['mn_%s integer' % x for x in self._get_mnemonics()])

  def get_sql_select(self, in_repositories=None, include_signature=False):
    statement = "SELECT function_text_id, "
    if include_signature:
      statement += " function_text.signature, "
    statement += self.get_sql_columns() + " FROM " + self.get_sql_table()
    if include_signature:
      statement += " JOIN function_text ON function_text_id = function_text.id "
    t, i = self._sql_select_apply_filter(in_repositories=in_repositories)
    statement += t
    return statement, i

class ArithCounter(MultiMnemonicCounterMetric):
  def __init__(self):
    super(ArithCounter, self).__init__(
      ['add', 'sub', 'mul', 'div', 'imul', 'idiv', 'inc', 'dec', 'neg',
       'sar', 'sal',
       'addl', 'subl'])
  
  def get_sql_table(self):
    return 'arith_counter_metric'

class BitOpCounter(MultiMnemonicCounterMetric):
  def __init__(self):
    super(BitOpCounter, self).__init__(
      ['shr', 'shl', 'shld', 'shrd', 'ror', 'rol', 'rorl', 'roll',
       'rcr', 'rcl',
       'and', 'or', 'xor', 'not'])
    
  def get_sql_table(self):
    return 'bitop_counter_metric'

class JmpCounter(MultiMnemonicCounterMetric):
  def __init__(self):
    #TODO fix metrics
    super(JmpCounter, self).__init__(
       ['jmp',
        'je', 'jne',
        'jz', 'jnz',
        'jg', 'jge',
        'ja', 'jae',
        'jl', 'jle',
        'jb', 'jbe',
        'jo', 'jno',
        'js', 'jns',
        'loop', 'loope', 'loopne', 'loopnz', 'loopz'
        ])

  def get_sql_table(self):
    return "jmp_counter_metric"

class CallCounter(MultiMnemonicCounterMetric):
  def __init__(self):
    super(CallCounter, self).__init__(['call'])
  
  def get_sql_table(self):
    return "call_counter_metric"

counter_metrics = {
  'expensive': MultiMnemonicCounterMetric,
  'arithmetic': ArithCounter,
  'logical': BitOpCounter,
  'jumps': JmpCounter,
  'calls': CallCounter
}
