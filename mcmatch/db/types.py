'''
Core ORM types

@author: niko
'''

from compileroptions import CompilerOptions
from mcmatch.matchers import MyersSequenceMatcher
from mcmatch.levenshtein import levenshtein
import subprocess, collections, os
from __builtin__ import isinstance
import logging
from mcmatch.x86 import jump_mnemonics
import re

class ObjectInfo:
  """Represents the information of an object file."""

  id = None
  locked = False
  
  def __init__(self, object_path, mtime=None, function_list=None,
               normalize_path=True, id=None):
    """Create an instance.

    @type object_path: str
    @param object_path: specifies the path to the object file.
    @param mtime: if not None, the modification time will be set from the object file on disk
    @type normalize_path: list
    @param function_list: if not None, it must be a list of L{Fn} instances, describing the list of functions contained
                          in this object.
    @type normalize_path: bool
    @param normalize_path: perform object_path normalization using L{os.path.abspath}.

    """
    if normalize_path:
      self.object_path = os.path.abspath(object_path)
    else:
      self.object_path = object_path

    if mtime is None:
      self.mtime = os.stat(self.object_path).st_mtime
    else:
      self.mtime = mtime

    if isinstance(function_list, list):
      self.function_list = function_list
    else:
      self.function_list = []

    self.compileopts = None
    if id is not None:
      self.id = id

  def get_mtime(self):
    return self.mtime
  
  def get_functions_by_shortname(self):
    """
    Returns a list of all functions as L{Fn} instances.

    TODO: add filtering capabilities"""
    return self.function_list

  def add_function(self, function):
    """Add an L{Fn} instance to the function list."""
    assert isinstance(function, Fn)
    self.function_list.append(function)

  def set_compileopts(self, compileopts):
    """Associate L{CompilerOptions} with this object file."""
    assert isinstance(compileopts, CompilerOptions)
    self.compileopts = compileopts

  def get_compileopts(self):
    """rtype: CompilerOptions
    
    returns the CompilerOptions object associated
    with this object, or a new CompilerOptions() object
    if no compileroptions exist.
    """
    if not self.compileopts:
      self.compileopts = CompilerOptions()
    return self.compileopts

  def get_path(self):
    """return the path this object was stored at."""
    return self.object_path

class DisassemblyLine:
  """Class representing a single assembly instruction."""
  pos_abs = 0
  pos_rel = 0
  op = ''
  params = ''
  comment = ''
  
  def is_conditional_jump(self):
    return self.op != 'jmp' and self.op in jump_mnemonics

  def is_unconditional_jump(self):
    return self.op == 'jmp'

  def is_jump(self):
    return self.op in jump_mnemonics
  
  def get_jump_offset(self, abort_on_error=False):
    """Attempts detection of the jump offset.

    This is done by first attempting to identify an absolute jump address,
    or, if that fails, a relative jump address.
    
    @return: The relative jump distance, in bytes (negative for backward jumps).
    """
    if not (self.is_conditional_jump() or self.is_unconditional_jump()):
      if abort_on_error:
        raise RuntimeError("Not a jump")
      else:
        return 0
    
    if len(self.params) == 1:
      jumptgt_abs = re.compile("^0x([0-9a-fA-F]+)$")
      m = jumptgt_abs.match(self.params[0])
      if m:
        return self.pos_abs - int(m.group(1), 16)

    jumptgt = re.compile(".*([+-]\d+)$").match(self.comment)
    if not jumptgt:
      # assume jump to start.
      if abort_on_error:
        raise RuntimeError("Cannot reliably identify jump target: " + self.comment)
      else:
        logging.error("Cannot reliably identify jump target: %r %r --> %r " %(
                                                self.op, self.params, self.comment))
        return 0
    
    return int(jumptgt.group(1))  - self.pos_rel
    
  def from_line(self, line):
    """Create an instance from a standard gdb disassembly line,
    in the format 0x(absolute address) <(+relative address)> mnemonic [parameters] [comments]"""
    if not len(line):
      return
    tokens = line.split()
    self.line = line
    # try to figure out what the tokens mean.
    
    if tokens[0].startswith("0x"):
      self.pos_abs = int(tokens[0], 16)
    else:
      logging.warning("unable to parse disassembly line %s (missing pos_abs)" % line)
    
    if tokens[1].startswith("<+") and tokens[1].endswith(">:"):
      self.pos_rel = int(tokens[1][2:-2])
    else:
      logging.warning("unable to parse disassembly line %s (missing pos_rel)" % line)
    
    self.op = tokens[2]
    
    if self.is_conditional_jump() or self.is_unconditional_jump() and tokens[-1][0] == '<'\
      and tokens[-1][-1] == '>':
      self.comment = tokens[-1][1:-1]
      del tokens[-1]
    
    self.params = tokens[3:]
    
    
class Codeblock(object):
    """Encapsulates a set of disassembly lines."""
    disassembly = None
    disassembly_nlines = None
    metrics = None
    compileopts = None

    def disassembly_from_text(self, text):
      """Set instances content from a block of text in gdb-format,
      with newlines separated by "\n".
      """
      if text is None:
        self.disassembly = []
      else:
        self.disassembly = text.split("\n")
        self.disassembly_nlines = len(self.disassembly)

    def disassembly_to_text(self):
      """Get instances content as a block of text in gdb-format."""
      if self.disassembly is None:
        return ""
      return "\n".join(self.disassembly)
      

    def calculate_metrics(self, force=True):
      """Calculate all known metrics.

      if force is set to True, metric will be updated even if
      metrics already exist."""

      # TODO re-implement calculate_metrics/rename to import_metrics_from_database
      raise Exception("calculate_metrics needs to be re-implemented")


    def metric_euclidean_diff_to(self, fnb, scaling=None):
      """Create euclidean difference to a separate object."""
      self.calculate_metrics()
      fnb.calculate_metrics()
      a = 0
      ab = 0
      for m in self.metrics['mc']:
        d = self.metrics['mc'][m] - fnb.metrics['mc'][m]
        if scaling is not None and m in scaling:
          d *= scaling[m]
        a += pow(d, 2)
        ab += self.metrics['mc'][m] + fnb.metrics['mc'][m]
      a = pow(a, 0.5) # too lazy to go to the top of the file and import math
      return (a, ab)

    def hist_euclidean_diff_to(self, fnb, scaling=None):
      hist_a = self.get_mnemonic_histogram()
      hist_b = fnb.get_mnemonic_histogram()

      instrs = set(hist_a.keys() + hist_b.keys())
      a = 0
      for instr in instrs:
        sf = 1.0
        va = 0
        vb = 0
        if (scaling is not None) and instr in scaling:
          sf = scaling[instr]
        if instr in hist_a:
          va = hist_a[instr]
        if instr in hist_b:
          vb = hist_b[instr]
        a += pow((va - vb)*sf, 2)
      a = pow(a, 0.5)
      return (a,)


    # include absolute adress in the diff
    DIFF_ABSADDR   = 1 # not implemented
    # include relative adress in the diff
    DIFF_RELADDR   = 2 # not implemented
    # include mnemonic in the diff
    DIFF_MNEMONIC  = 4
    # include opcode in the diff (extended mnemonic)
    DIFF_OPCODE    = 8 # not implemented
    # include opcode parameters in the diff
    DIFF_PARAMETERS = 16
    def diff_disassembly(self, other, flags = None):
        """Compares the disassembly of Fn with the disassembly
        in other (needs to exist). Optionally, DIFF_* flags
        can be specified. Returns a tuple
        (match ratio, longest match size)"""
        if flags == None:
            flags = self.DIFF_MNEMONIC | self.DIFF_PARAMETERS
        if other.disassembly is None:
            print "Error: other (", other.name, ") does not have disassembly attached"

        a = self.prep_disassembly(self.disassembly, flags)
        b = self.prep_disassembly(other.disassembly, flags)

        sm = MyersSequenceMatcher(a=a, b=b)
        return (sm.ratio(),
                0) #sm.find_longest_match(0, len(a), 0, len(b))[2])

    def prep_disassembly(self, lines, flags):
        """Return a list representation of tokenized instructions from a list of
        instructions given in 'lines'.
        Each list entry contains the tokens included through bitwise-or'ing the
        flags parameter with the DIFF_*-constants."""
        new_lines = []
        for line in lines:
          elems = line.split()
          new_str_elems = []
          try:
            if flags & self.DIFF_ABSADDR:
                new_str_elems.append(elems[0])
            if flags & self.DIFF_RELADDR:
                new_str_elems.append(elems[1])
            if flags & self.DIFF_MNEMONIC:
                new_str_elems.append(elems[2])
            if flags & self.DIFF_PARAMETERS:
                new_str_elems.append(" ".join(elems[3:]))
            new_lines.append(" ".join(new_str_elems))
          except IndexError:
            logging.error("malformed assembly line: %s" % line)
        return new_lines

    def get_mnemonic_list(self):
      """return a list of the mnemonic parts of all instructions of this object."""
      if not self.disassembly:
        raise Exception("Instance does not contain disassembly.")
      return self.prep_disassembly(self.disassembly, self.DIFF_MNEMONIC)

    def get_mnemonic_histogram(self):
      """return a dictionary of the number of occurences of all mnemonics in this instance."""
      l = self.get_mnemonic_list()
      d = collections.defaultdict(int)
      for x in l: d[x] += 1
      return d

class Fn(Codeblock):
    """Represents a function instance.

    This class extends Codeblock with information related to a function in an object,
    such as the function signature and the containing object."""
    sig = None
    source_file = None
    function_id = None
    object_id = None

    @staticmethod
    def get_sql_select(disassembly=True):
      """Return the SQL SELECT columns required for the L{from_sql_row} function.
      
      @param disassembly: Include disassembled code
      """
      ret = """SELECT
        functions.id, functions.name, functions.signature,
        functions.source_file, functions.objectID, functions.function_text_lines"""
      if disassembly:
        ret += ", function_text.disassembly"
      ret += " FROM functions"
      if disassembly:
        ret += """
          LEFT OUTER JOIN
            function_text
          ON
            functions.function_text_id = function_text.id"""
      return ret
    
    @classmethod
    def from_sql_row(cls, row, disassembly):
      """Create a new Fn instance from a list or tuple containing
      the columns, as retrieved the columns defined by L{get_sql_select}.

      @param disassembly: Include disassembly. If set to True, get_sql_select must be called
                          with disassembly=True as well."""
      fn_id = row[0]
      name = row[1]
      sig = row[2]
      source = row[3]
      object_id = row[4]
      n_lines = row[5]

      fn = Fn(name, sig, source, object_id)
      fn.function_id = fn_id
      fn.object_id = object_id
      fn.disassembly_nlines = n_lines
      if disassembly:
        fn.disassembly_from_text(row[6])
      return fn

    def __init__(self, name, full_sig, source_file, object_id=None):
      """Create a new instance.

      @param name: The function name
      @param full_sig: The full signature
      @param source_file: Path to the source file
      @param object_id: The id of the containing object, if known"""

      if object_id is not None:
        assert isinstance(object_id, int)
      self.name = name
      self.sig = full_sig
      self.object_id = object_id
      self.source_file = source_file

    def get_container_object_id(self):
      """Raises Exception if this has no object_id assigned to it.
      This should only be the case during extraction from an object file"""
      if self.object_id is None:
        raise Exception("get_container_object_id called on temporary")
      return self.object_id

    def length(self):
      """Return the length of the text form of the disassembled code,
      in bytes."""
      if not self.disassembly:
        return 0
      return len(self.disassembly)

    def get_shortinfo(self, compileroptions=None, db=None):
      """returns a short string representing the function.
      
      @param compileroptions: A L{CompilerOptions} instance, to be included in the shortinfo text.
      @param db: A L{FunDB} instance that is queried when L{CompilerOptions} is None. If
                 neither compileroptions nor db is set, "???" will be displayed instead of compiler/optimization level.
      """
      if compileroptions is None and db is not None:
        compileroptions = db.get_compiler_options(self.object_id)
      ret = self.name
      compile_string = "/???"
      if compileroptions is not None:
        compile_string = "/" + compileroptions.get_shortinfo()

      ret += compile_string

      if self.disassembly_nlines is None:
        ret += "[len=?]"
      else:
        ret += "[len=%d]" % self.disassembly_nlines
      if self.object_id is None:
        ret += "@N/A"
      else:
        ret += "@%d" % self.object_id
      return ret

    def get_shortinfo_html(self, compileroptions=None, db=None):
      """As get_shortinfo, but as a HTML representation to be used with the built-in webserver"""
      return "<a href='/fn?id=%d'>%s</a>" % (self.function_id, self.get_shortinfo(compileroptions, db))

    def set_compileopts(self, opts):
      """Update the compileroptions for this instance."""
      if not isinstance(opts, CompilerOptions):
        raise "set_compileopts requires a CompilerOptions parameter"
      self.compileopts = opts

    def match_shortinfo(self, opts):
      """Return True if this function matches the compiler options according to
      L{CompilerOptions.match_shortinfo}. Returns also True if the argument is empty,
      Returns False if this instance has no compiler options attached.

      @param opts: The options to match."""
      # TODO make this include function name
      opts = opts.strip()
      if len(opts) == 0:
        return True
      # TODO move this to object
      if not self.compileopts:
        return False # len(opts) > 0!
      return self.compileopts.match_shortinfo(opts)


class FnDiff(object):
  """A utility class for 1:1 comparison of two functions."""
  ratio_diff = None
  ratio_diff_szd = None
  longest_block_sz = None
  fnalen = None
  fnblen = None

  def __init__(self, fna, fnb):
    """Initialize with two L{Fn} instances."""
    assert isinstance(fna, Fn)
    assert isinstance(fnb, Fn)
    self.fna = fna
    self.fnb = fnb

  def make_diffstats(self):
    ratio, longestblock = self.fna.diff_disassembly(self.fnb, Fn.DIFF_MNEMONIC)
    self.ratio_diff = ratio
    self.longest_block_sz = longestblock
    self.fnalen = len(self.fna.disassembly)
    self.fnblen = len(self.fnb.disassembly)
    self.ratio_diff_szd = (self.ratio_diff * 
                (float(min(self.fnalen, self.fnblen))/max(self.fnalen,self.fnblen)))
    self.levenshtein = levenshtein(self.fna.disassembly, self.fnb.disassembly)
    self.normalized_levenshtein = 1.0*self.levenshtein/((self.fnalen + self.fnblen)/2.0)
  
  def make_opcode_stats(self):
    """TODO: Create histogram of occurences of each mnemonic.
    (also, relative occurences of each opcode)"""
    pass

  def get_long_descr(self):
    print "A: '%s' (%d) in %s (defined in %s)" % (
        self.fna.name, self.fnalen, self.fna.in_object, self.fna.source_file)
    print "B: '%s' (%d) in %s (defined in %s)" % (
        self.fnb.name, self.fnblen, self.fnb.in_object, self.fnb.source_file)
    print "diff.ratio:           ", self.ratio_diff
    print "diff.ratio*sizeratio: ", self.ratio_diff_szd
    print "diff.longestblock:    ", self.longest_block_sz
    print "diff.levenshtein:     ", self.levenshtein 
    print "A most common mnemonics:"
    da = self.fna.get_mnemonic_histogram()
    db = self.fnb.get_mnemonic_histogram()
    for va in sorted(da, key=da.get, reverse=True)[:3]:
      print va, da[va], "%3.1f%%" % (100*float(da[va])/self.fnalen)
    print "B most common mnemonics:"
    for vb in sorted(db, key=db.get, reverse=True)[:3]:
      print vb, db[vb], "%3.1f%%" % (100*float(db[vb])/self.fnblen)

class FnMetric(object):
  def __init__(self):
    pass

  def get_kv(self):
    """Return a key/value pair describing this metric."""
    raise NotImplementedError()
  
  def get_sql_table(self):
    raise NotImplementedError()
  
  def get_sql_columns(self, fq_select=True, fq_rename=False):
    """Get the SQL columns for this metric.
    If fq_select is True, the columns will be fully qualified (sqltable.column).
    If fq_rename is True, each column will include a "AS sqltable_column".
    """
    raise NotImplementedError()

  def get_sql_contents(self):
    raise NotImplementedError()

  def _sql_select_apply_filter(self, function_text_id="function_text_id", in_repositories=None):
    """
    function_text_id should be the fully qualified name of the function_text_id column. The
    default value should be sufficient in non-ambigous conditions.

    returns a tuple (" WHERE ...", [additional, values, for, inputtuple])"""
    if in_repositories is not None:
      return """ WHERE """ + function_text_id + """ IN (
          SELECT functions.function_text_id FROM objects
            JOIN functions ON functions.objectid = objects.id
           WHERE objects.repository = ANY(%s))""", in_repositories
    return "", []

  def _sql_prep_cols(self, columns, sqltable, fq_select, fq_rename):
    if fq_select or fq_rename:
      if fq_select:
        columns = [sqltable + "." + c for c in columns]
      if fq_rename:
        columns = [c + " AS " + c.replace('.', '_') for c in columns]
    return columns
  
  def get_sql_select(self, in_repositories=None, include_signature=False):
    statement = "SELECT function_text_id, "
    data_offset = 1
    if include_signature:
      data_offset += 1
      statement += "function_text.signature, "
    statement += ", ".join(self.get_sql_columns()) + " FROM " + self.get_sql_table()
    if include_signature:
      statement += " JOIN function_text ON function_text_id = function_text.id "
    t, i = self._sql_select_apply_filter(in_repositories=in_repositories)
    statement += t
    return statement, i, data_offset

  def calculate(self, fn):
    assert isinstance(fn, Codeblock)
    raise NotImplementedError()
    return None

  def create_table_ddl(self):
    raise NotImplementedError()
  
