'''
CompilerOptions class and related functionality

@author: niko
'''
import logging

class CompilerOptions(object):
  """Class representing the compile time options of an object file.
  Currently stores compiler name, optimization level and -static."""
  compiler = None # type: str
  compiler_version = None # type: str
  opt = None # type: str
  repository = None # type: str
  is_static = None # type: bool
  
  @classmethod
  def from_sql_row(cls, row):
    opt = cls()
    opt.compiler = row[0]
    opt.compiler_version = row[1]
    opt.opt = row[2]
    opt.is_static = row[3]
    opt.repository = row[4]
    return opt
  
  @staticmethod
  def get_sql_field_count():
    return 5
    
  @staticmethod
  def get_sql_field_names(as_list=False, as_update_s=False):
    fields = ['compiler', 'compiler_version', 'opt_level', 'is_static', 'repository']
    if as_update_s:
      fields = [f + " = %s" for f in fields]
    if as_list:
      return fields
    return ' ' + ", ".join(fields) + ' '
  
  def get_sql_field_data(self):
    return [self.compiler, self.compiler_version, self.opt, self.is_static, self.repository]
  
  def __init__(self):
    pass

  def set_optlevel(self, opt):
    if opt is None:
      return None
    opt_ = str(opt).strip()
    if opt_.startswith("-"):
      opt_ = opt_[1:]
    if opt_.startswith("O"):
      opt_ = opt_[1:]
    if len(opt_) > 1:
      raise Exception("Invalid optimization level passed: " + opt)
    self.opt = opt_

  def set_compiler(self, compilername):
    self.compiler = compilername
    
  def get_compiler(self):
    return self.compiler
    
  def set_static(self, static):
    assert isinstance(static, bool)
    self.is_static = static
  
  def get_optlevel(self):
    return self.opt
  
  def set_repository(self, repository):
    self.repository = repository
  
  def get_repository(self):
    return self.repository
  
  def get_shortinfo(self):
    if self.compiler is None:
      # this happens if the corresponding fields in the
      # database are NULL, aka unset.
      ret = "null"
    else:
      ret = self.compiler
    flags = []
    if self.opt:
      flags.append("O%s" %self.opt)
    if self.is_static:
      flags.append("static")
    if len(flags):
      ret += "(" + (",".join(flags)) + ")"
    return ret

  @staticmethod
  def __consume_between(s, a, b):
    """Process string s, return a tuple:
      - the remaining string with a space where [a..b] was
      - the substring between a and b from s"""
    if not ((a in s) and (b in s)):
      return (s, '')
    start = s.index(a) + len(a)
    end = s.index(b, start)
    between = s[start:end]
    rest = s[start-1:] + ' ' + s[end+1:]
    return (rest, between)

  def match_shortinfo(self, string):
    # reverse get_shortinfo:
    string, flags = self.__consume_between(string, "(", ")")
    if len(flags):
      flags = flags.split(",")
      for flag in flags:
        if flag.startswith("O"):
          if self.opt != flag[1:]:
            return False
        elif flag == "static" and not self.is_static:
          return False
        else:
          raise Exception("Don't know what to do with flag %s in %s." % (flag, flags))

    string, disasmlen = self.__consume_between(string, "[", "]")
    # ignore disasmlen.
    string = string.strip()
    if ' ' in string:
      raise Exception("After consuming compiler option string, could not find compiler name. Got '%s'." % string)

    if self.compiler != string:
      return False
    return True

  @classmethod
  def from_string(cls, optstring):
    """parse a string such as 'gcc -O2 -static -g', extract compile flags from it
    and return a new CompilerOptions object."""
    tokens = optstring.strip().split()
    if len(tokens) == 0:
      raise "Received empty compiler optstring"

    # Check whether our first token is a known compiler. TODO: Get version.
    is_known_compiler = True in [tokens[0].startswith(comp) for comp in ['gcc', 'g++', 'clang', 'clang++']]
    if not is_known_compiler:
      logging.warning("'%s' is not a known compiler, verify that your optstring is correct please" % tokens[0])
      compiler = "unknown"
    else:
      compiler = tokens[0]
      tokens = tokens[1:]

    co = cls()
    co.set_compiler(compiler)
    
    if '-static' in tokens:
      tokens.remove('-static')
      co.set_static(True)

    # find optimization level
    opttoken = None
    for token in tokens:
      if token.startswith("-O"):
        co.set_optlevel(token)
        opttoken = token 
        break
    if opttoken is not None:
      tokens.remove(opttoken)

    # ignore some other flags that don't matter to us
    if "-w" in tokens:
      tokens.remove("-w")
    if "-g" in tokens:
      tokens.remove("-g")

    # print all ignored tokens as a notice
    if len(tokens):
      logging.info("could not parse the following tokens in optimization string: %s" % tokens)

    return co


