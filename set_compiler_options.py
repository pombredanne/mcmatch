#!/usr/bin/python2
import logging, argparse
from mcmatch.db.pg_database import PgFunDB as DB
from mcmatch.db.compileroptions import CompilerOptions
import os
from IPython.core.release import description

def main():
  logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  parser = argparse.ArgumentParser(description='set compile options for the given objects')
  #parser.add_argument('-s', '--opt-string', type=str, dest='optstring', action='store', required=True,
  #    help='compiler command line parameters (for example, gcc -O2 -static)')
  parser.add_argument('-O', '--opt-level', type=str, help='optimization level', dest='optlevel', default=None)
  parser.add_argument('-c', '--compiler', type=str, help='compiler name', dest='compiler', default=None)
  parser.add_argument('-v', '--compiler-version', type=str, help='compiler version', dest='compiler_version', default=None)
  parser.add_argument('-r', '--repository', type=str, help='set repository (ex.: git-1.1)', default=None)
  parser.add_argument('objfiles', metavar="f.o", type=str, nargs='+', help='object files to update') 
  args = parser.parse_args()

  #compopts = CompilerOptions.from_string(args.optstring)
  compopts = CompilerOptions()
  compopts.compiler = args.compiler
  compopts.compiler_version = args.compiler_version
  compopts.opt = args.optlevel
  compopts.repository = args.repository
  logging.info("setting %s on %d objects" % (compopts.get_shortinfo(), len(args.objfiles)))

  db = DB()
  
  counter = 0
  for obj in args.objfiles:
    obj = os.path.abspath(obj)
    mtime = os.stat(obj).st_mtime
    result = db.set_compiler_options_by_path(obj, mtime, compopts)
    if result:
      counter += 1
    else:
      logging.warning("no update performed on object %s." % obj)

  db.save()

  logging.info("Updated compiler info for %d file(s)" % counter)
if __name__ == '__main__':
  main()
