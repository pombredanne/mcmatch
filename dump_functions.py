from mcmatch.db.types import FnDiff
from mcmatch.db.pg_database import PgFunDB as DB
import cPickle as pickle
import logging
import re
import sys
import argparse

def main():
  logging.basicConfig(level=logging.INFO)
  
  parser = argparse.ArgumentParser(description='dump objectfile/function structure from the database')
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
  args = parser.parse_args()

  if len(args.function_filter) == 0 or len(args.object_filter) == 0:
    args.require_both = False

  fundb = DB()
  x_all_fns = list(fundb.all_functions())
  all_fns = []
  allfn_namefilter_active = len(args.function_filter) > 0 or len(args.object_filter) > 0

  if len(args.object_filter):
    fundb.precache_containing_objects(None)
  
  if allfn_namefilter_active:
    for fn in x_all_fns:
      if len(fn.disassembly) < args.min_length:
        continue
      fname_matches = True in [filt in fn.name for filt in args.function_filter]
      objnm_matches = True in [filt in fn.in_object for filt in args.object_filter]

      if args.require_both:
        if fname_matches and objnm_matches:
          all_fns.append(fn)
      else:
        if fname_matches or objnm_matches:
          all_fns.append(fn)
  else:
    all_fns = x_all_fns
  del x_all_fns

  if len(all_fns) == 0:
    logging.error("no functions to print")
    return

  # put functions back into an object dict
  objdict = {}
  for fun in all_fns:
    if not fun.object_id in objdict:
      objdict[fun.object_id] = []
    objdict[fun.object_id].append(fun)

  for objectid in objdict:
    obj = fundb.get_object(objectid)
    print obj.get_path()
    for fun in objdict[objectid]:
      print ">>", fun.get_shortinfo(obj.get_compileopts())

if __name__ == "__main__":
  main()
