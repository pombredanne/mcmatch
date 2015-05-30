import pprint
import subprocess
import sys
import logging
from mcmatch.db.types import Fn, FnDiff
from mcmatch.db.pg_database import PgFunDB as DB

import tempfile
def dump_disassembly_to_temp(fn, flags=None):
  f = tempfile.NamedTemporaryFile(delete=False)
  if flags == None:
    disassembly = "\n".join(fn.disassembly)
  else:
    disassembly = "\n".join(fn.prep_disassembly(fn.disassembly, flags))
  f.write(disassembly)
  f.close()
  return f.name

def print_stats(fna, fnb):
    fd = FnDiff(fna, fnb)
    fd.make_diffstats()
    fd.get_long_descr()

def main():
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    print "Usage:", sys.argv[0], " <function1> [function2]"
    return

  fdb = DB()

  fns = sys.argv[1:]
  funs = fdb.get_functions_by_shortname(fns)
  fnames = []
  for fun in funs:
    if funs[fun] is None:
      logging.error("One or more functions couldn't be found, for example %s." % fun)
      return
    fnames.append(dump_disassembly_to_temp(funs[fun], Fn.DIFF_MNEMONIC | Fn.DIFF_PARAMETERS ))

  if len(fnames) == 1:
    subprocess.call(['gedit', fnames[0]])
  elif len(fnames) == 2:
    print_stats(funs.values()[0], funs.values()[1])
    subprocess.call(['meld', fnames[0], fnames[1]])
  else:
    print "len(fnames) == %d (this is an error)" % len(fnames)

if __name__ == "__main__":
  main()
