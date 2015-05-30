#!/usr/bin/python2
from mcmatch.db.types import ObjectInfo, FnDiff
from mcmatch.db.pg_database import PgFunDB as DB
from mcmatch.util import NN2ProgressPrinter, NProgressPrinter
import logging
import argparse
from collections import defaultdict

def make_scaling(all_functions):
  counter = defaultdict(int)
  for fun in all_functions:
    hist = fun.get_mnemonic_histogram()
    for k in hist:
      counter[k] += hist[k]
  for k in counter:
    counter[k] = 1.0/counter[k]
  return counter

MODE_FNDIFF = 1
MODE_METRIC_EUCLID = 2
MODE_HIST_EUCLID = 3

def get_diff(db, fna, fnb, mode, scaling):
  if mode == MODE_FNDIFF:
    diff = FnDiff(fna, fnb)
    diff.make_diffstats()
    
    fna_si = fna.get_shortinfo(db.get_compiler_options(fna.object_id))
    fnb_si = fnb.get_shortinfo(db.get_compiler_options(fnb.object_id))
    
    return (diff.ratio_diff_szd, fna_si, fnb_si)
  if mode == MODE_METRIC_EUCLID:
    m = fna.feature_euclidean_diff_to(fnb, scaling)
    return (m[0], m[1], fna_si, fnb_si)
  if mode == MODE_HIST_EUCLID:
    m = fna.hist_euclidean_diff_to(fnb, scaling)
    return (m[0], fna_si, fnb_si)

def n_to_n_compare(db, all_fns, mode, scaling):
  """Compare every item to every other item. (O(n*(n/2)))"""
  l = []
  progress = NN2ProgressPrinter(len(all_fns))
  for fni in range(len(all_fns)):
    progress.bump()
    fna = all_fns[fni]
 
    logging.debug("processing %s" % fna.name)

    for fnj in range(fni+1, len(all_fns)):
      fnb = all_fns[fnj]
      l.append(get_diff(db, fna, fnb, mode, scaling))
  return l

def m_to_n_compare(db, fn_dict, all_fns, mode, scaling):
  """Compare every function in fn_dict (name->Fn) to every function in all_fns (list [Fn])"""
  l = []
  progress = NProgressPrinter(len(all_fns)*len(fn_dict))
  for fna_name in fn_dict:
    fna = fn_dict[fna_name]
    for fnbi in range(len(all_fns)):
      progress.bump()
      fnb = all_fns[fnbi]
      l.append(get_diff(db, fna, fnb, mode, scaling))
  return l

def main():
  logging.basicConfig(level=logging.INFO)
  
  parser = argparse.ArgumentParser(description='perform diff actions between functions in the database')
  parser.add_argument('-a', '--function-a', dest='function_a', action='append', default = [],
      help='compare given function to all others (filters apply). Can be specified multiple times.')
  parser.add_argument('-o', '--objects', dest='object_filter', action='append', default = [],
      help='only process functions in objects whose name contains this parameter. Can be specified multiple times to match name against any of the list.')
  parser.add_argument('-f', '--functions', dest='function_filter',
      action='append', default = [],
      help='only process functions with names containing this parameter. Can be specified multiple times (matches any of the parameters)')
  parser.add_argument('-b', '--both', help="""only include functions matching both object and function filter (instead of either/or).
      If there is not at least one filter for each, this option will do nothing.""",
      action='store_true', dest='require_both')
  parser.add_argument('-m', '--min-length', help='ignore functions with less instructions than this', default=5, type=int,
      action='store', dest='min_length')
  parser.add_argument('--mode', help='diff mode to use', choices=['diff-ratio', 'feature-default', 'feature-mncount'],
      action='store', dest='mode')
  parser.add_argument('-s', '--scale', help='use scaling for feature-* modes', action='store_true', dest='scale')
  args = parser.parse_args()

  if len(args.function_filter) == 0 or len(args.object_filter) == 0:
    args.require_both = False

  fundb = DB()
  logging.info("Loading functions")
  x_all_fns = fundb.all_functions()
  all_fns = []
  allfn_namefilter_active = len(args.function_filter) > 0 or len(args.object_filter) > 0

  if len(args.object_filter):
    fundb.precache_containing_objects(None)
  
  mode = MODE_FNDIFF
  if args.mode == 'feature-default':
    mode = MODE_METRIC_EUCLID
  elif args.mode == 'feature-mncount':
    mode = MODE_HIST_EUCLID
  elif args.mode is not None:
    raise Exception("something went wrong, got %s as --mode" % args.mode)

  scaling = None
  if args.scale:
    logging.info("collecting feature scaling information...")
    scaling = make_scaling(x_all_fns) 

  if allfn_namefilter_active:
    for fn in x_all_fns:
      if fn.disassembly and (len(fn.disassembly) < args.min_length):
        continue
      fname_matches = True in [filt in fn.name for filt in args.function_filter]
      objnm_matches = True in [filt in fundb.get_object(fn.get_container_object_id()).get_path() for filt in args.object_filter]

      if args.require_both:
        if fname_matches and objnm_matches:
          all_fns.append(fn)
      else:
        if fname_matches or objnm_matches:
          all_fns.append(fn)
  else:
    all_fns = list(x_all_fns)
  del x_all_fns

  logging.info("Loaded functions, initializing analysis")

  if len(all_fns) == 0:
    logging.warning("no functions to analyze")
    return

  l = []
  if len(args.function_a):
    fun_dict = fundb.get_functions_by_shortname(args.function_a) 
    # verify that there are actually functions to analyze
    has_fna = False
    for funname in fun_dict:
      if fun_dict[funname] is not None:
        has_fna = True
        break
    if not has_fna:
      logging.error("could not find any 'function a'")
      return
    l = m_to_n_compare(fundb, fun_dict, all_fns, mode, scaling)
  else:
    l = n_to_n_compare(fundb, all_fns, mode, scaling)

  print "done."
  l.sort(reverse=(mode == MODE_FNDIFF))
  
  for i in range(len(l)):
    print ("%.3f" % l[i][0]), l[i][1:]
  

if __name__ == "__main__":
  main()
