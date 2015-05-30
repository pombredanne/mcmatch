"""
Base database class and pickle-based implementation
"""
import os, subprocess
import collections, difflib
import cPickle as pickle
import logging
import pprint
from compileroptions import CompilerOptions
from mcmatch.matchers import MyersSequenceMatcher
from mcmatch.levenshtein import levenshtein
from mcmatch.db.types import ObjectInfo


class FunDB():
  function_count = None
  last_instance = None
  
  def __init__(self):
    FunDB.last_instance = self
  
  def load(self):
    """Import data from the DB if required."""
    pass
  
  def save(self):
    """Commit changes to the database"""
    pass
  
  def get_function_count(self):
    """Returns the amount of registered functions"""
    pass
  
  def needs_update(self, object_file_name):
    """Tests object_file_name and checks the result against the database,
    returning True if the object file is newer than the object file info
    in the database"""
    pass
  
  def store_object(self, objectinfo):
    """Store the updated ObjectInfo object"""
    pass
  
  def all_functions(self):
    """returns an iterable that yields all functions defined"""
    pass
  
  def _get_functions_get_name_to_opts_map(self, functions):
    """return a dictionary mapping from function name to
    all defined options"""
    function_names = {}
    for f in functions:
      if "/" in f:
        name, opts = f.split("/")
        if not name in function_names:
          function_names[name] = []
        function_names[name].append(opts)
      else:
        if not f in function_names:
          function_names[f] = []
        function_names[f].append('')
    return function_names
  
  def _get_functions_slow(self, functions, debug):
    # this might be the most horrible piece of code in this codebase as of Oct 20 2014.
    # If there are filters in the function name, this dictionary
    # will map to the filter string, or to an empty string otherwise.
    function_names = self._get_functions_get_name_to_opts_map(functions)
    
    # register requested function names for output
    ret = {}
    for f in functions:
      ret[f] = []
    
    for f in self.all_functions():
      if f.name in function_names:
        for opts in function_names[f.name]:
          if f.match_shortinfo(opts):
            # rebuild the opts string if required:
            if len(opts):
              ret[f.name + "/" + opts].append(f)
            else:
              ret[f.name].append(f)
          else:
            logging.error("function %s does not match opts %s" % (f.get_shortinfo(), opts))
    
    # function-not-found & multiple-functions-found error handling
    for f in ret:
      if len(ret[f]) == 0:
        logging.error("couldn't find function %s" % f)
        ret[f] = None
      elif len(ret[f]) > 1:
        logging.warning("multiple functions found for %s:" % f)
        # TODO remove duplicates from same source file
        for o in ret[f]:
          logging.warning("  %s Object: %s\tSource: %s" % (o.get_shortinfo(), o.in_object, o.source_file))
        logging.warning("using first match only.")
        ret[f] = ret[f][0]
      else:
        ret[f] = ret[f][0]
      
    if debug:
      print "Found matches:" 
      for o in ret:
        if ret[o] is None:
          continue
        print "  %s Object: %s\tSource: %s" % (ret[o].get_shortinfo(), ret[o].in_object, ret[o].source_file)
    return ret
  
  def get_functions_by_shortname(self, functions, debug=True):
    """Accepts a list of functions, returns a dictionary
    mapping function name to a single corresponding Fn object,
    None if no such function exists. If multiple functions with
    the same name exist, only the first one found will be returned
    and a warning will be logged. Each function name may contain
    a '/' followed by extra information as returned from
    CompilerOptions.get_shortinfo() to narrow down the match."""
    pass
  
  def delete_objects_by_filename(self, filename):
    """Delete an object file and all associated functions"""
    pass
  
  def set_compiler_options(self, objfile, compileroptions):
    """Set compiler options for the given objectfile"""
    pass



class PickledFunDB(object):
  prefix = "/home/niko/dev/ma-testbench/"
  objects_fn = "objects.pickle"

  @staticmethod
  def load_pickle_file(filename, default=None):
    logging.debug("loading %s" % filename)
    try:
      f = open(filename, 'r')
    except IOError:
      return default
    data = pickle.load(f)
    f.close()
    return data

  @staticmethod
  def save_pickle_file(filename, data):
    f = open(filename, 'w')
    pickle.dump(data, f)
    f.close()

  def update_function_count(self):
    self.function_count = 0
    for obj in self.object_files:
      self.function_count += len(self.object_files[obj]['functions'])

  def __init__(self):
    logging.info("Loading database")
    self.object_files = FunDB.load_pickle_file(
        self.prefix + self.objects_fn, {})
    self.update_function_count()
    logging.info("Loaded %d functions in %d object files", self.function_count,
        len(self.object_files))

  def save(self):
    logging.info("Saving database")
    FunDB.save_pickle_file(self.prefix + self.objects_fn, self.object_files)
    self.update_function_count()
    
    logging.info("Stored %d functions in %d object files", self.function_count,
        len(self.object_files))

  def needs_update(self, objpath):
    """Determines whether a given object file needs updating"""
    objpath = os.path.abspath(objpath)
    curtime = os.stat(objpath).st_mtime
    objlastmod = 0
    if objpath in self.object_files:
      objlastmod = self.object_files[objpath]['mtime']
    if curtime > objlastmod:
      return True
    return False

  def update_object_by_filename(self, objpath, fnlist):
    objpath = os.path.abspath(objpath)
    if objpath in self.object_files:
# TODO as soon as we start storing stat info, existing info must be deleted here
      pass
    self.object_files[objpath] = {'mtime': os.stat(objpath).st_mtime,
        'functions': fnlist}

  def store_object(self, objectinfo):
    assert isinstance(objectinfo, ObjectInfo)
    self.update_object_by_filename(objectinfo.get_path(), objectinfo.function_list)
    
    
  def all_functions(self):
    for obj in self.object_files:
      for f in self.object_files[obj]['functions']:
        yield f

  def get_functions_by_shortname(self, functions, debug=True):
    return self._get_functions_slow(functions, debug)
    

  def __check_objfile_exists(self, objfile):
    if objfile not in self.object_files:
      raise KeyError("could not find object file" + objfile)

  def delete_objects_by_filename(self, objfile):
    """Delete object by path/file and all associated functions.
    
    Raises KeyError if the object does not exist."""
    self.__check_objfile_exists(objfile)
    del self.object_files[objfile]
 
  def set_compiler_options(self, objfile, compileroptions):
    """TODO verify code & data layout here. First of all, this function does not
    belong in the PickledFunDB class, rather, the PickledFunDB should have a get-objectfile or
    get-functions-by-objectfile method. Secondly, it is redundant to store the
    CompilerOpt object per function, as these options are inherently per-object.
    On the other hand though, each function then requires a backpointer to the
    object, as analyses are done on a function level, where this information is
    required. This currently only given by the in_object parameter, which under
    certain circumstances stores only the filename, not the full path (ambiguity),
    also, a full lookup for the object through the database might be time-consuming.
    
    Anyway, this function sets the CompilerOptions object for every function in this object,
    and raises KeyError if the object file does not exist in the DB."""
    self.__check_objfile_exists(objfile)

    fns = self.object_files[objfile]['functions']
    for fun in fns:
      fun.set_compileopts(compileroptions)
