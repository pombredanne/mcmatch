from mcmatch.db.types import Fn, ObjectInfo
from mcmatch.db.pg_database import PgFunDB as DB
import os, sys
import subprocess
import re
import logging
from _collections import defaultdict
from test.test_descrtut import defaultdict2
from mcmatch.util import replace_function_name

fdb = None

def identify_file(filename):
  cmd = ['file', '-b', '-e', 'cdf', '-e', 'ascii', '-e', 'apptype', '-e', 'tokens', '-e', 'tar']
  cmd.append(filename)
  output = subprocess.check_output(cmd).strip()
  return output

def is_elf(filename):
  return identify_file(filename).lower().startswith("elf")

def extract_disassemblies(objectfile, function_list):
  cmdline = ['gdb', '-batch', objectfile, '-ex', 'set disassembly-flavor intel']
  for fun_name in function_list:
    cmdline.extend(['-ex', "disassemble " + fun_name])
  print "gdb extracting %d functions from %s" % (len(function_list), objectfile)
  output = subprocess.check_output(cmdline).strip().split("\n")
  all_disassemblies = {}
  current_disassembly = []
  current_function = ""
  
  start_dump_str = "Dump of assembler code for function "

  for line in output:
    if line.startswith(start_dump_str):
      current_disassembly = []
      current_function = line.strip()[len(start_dump_str):-1]
    elif line.startswith("End of assembler dump."):
      all_disassemblies[current_function] = current_disassembly
    elif line.strip().startswith("0x"):
      current_disassembly.append(line.strip())
    else:
      logging.error("received unexpected line: %s" % (line.strip()))
      print output
      print cmdline
  return all_disassemblies


def map_symbols_to_api_functions(objectfile):
  """takes the object file to work on as parameter.
  returns a mapping from all known symbols of that
  objectfile to a list of "global" names for that
  same function. Global in that context are
  - "global" ELF symbols, that do not start with underscore
  - "local" ELF symbols that do not start with underscore
  if no such function names exist, there is *one* function
  name returned from the global table, and,
  if no such function exists, from the local table.
  In this case, if there are multiple possibilities, the
  shortest name is returned, and if multiple exist thereof,
  the smallest w.r.t. str.__cmp__.
  """
  cmd = ['objdump', '-j', '.text', '-t', objectfile]
  output = subprocess.check_output(cmd).strip()
  lines = output.split("\n")
  assert lines[0].startswith(objectfile)
  assert len(lines[1].strip()) == 0
  assert lines[2].startswith("SYMBOL TABLE:")
  lines = lines[3:]
  functions = defaultdict(list)
  for line in lines:
    line = line.strip()
    if not len(line):
      break
    addr_end = line.find(" ")
    addr = line[0:addr_end]
    line = line[addr_end:].strip()
    section_flag = line.find(".text")
    # objdump has 7 flags, followed by one space
    # .text should be at position 8.
    # We're missing a couple of symbols though.
    if section_flag == -1 or section_flag > 8:
      continue
    flags = line[0:section_flag]
    sym = line.rsplit(" ", 1)[1]
    if sym.find(".") != -1:
      sym = sym[:sym.find(".")]
    
    if 'w' in flags or 'g' in flags:
      functions[addr].append(('override', sym))
    else:
      functions[addr].append(('strong', sym))

  def symsort(a, b):
    '''compare length, or, if equal, the string itself.'''
    if len(a) == len(b):
      return cmp(a, b)
    return cmp(len(a), len(b))
  
  mapping = {}
  
  for addr in functions:
    fsyms = functions[addr]
    local = [z[1] for z in fsyms if z[0] == 'strong']
    overrides = [z[1] for z in fsyms if z[0] == 'override']
    
    is_public = lambda f: not f.startswith("_")
    local_public = filter(is_public, overrides)
    overrides_public = filter(is_public, overrides)
    
    result = overrides_public
    if not len(result):
      result = local_public
    if not len(result) and len(overrides):
      overrides.sort(cmp=symsort)
      result = [overrides[0]]
    if not len(result) and len(local):
      local.sort(cmp=symsort)
      result = [local[0]]
    if not len(result):
      raise Exception("Programming error - no symbols available for address")
    
    all_names = set(local + overrides)
    for name in all_names:
      mapping[name] = result
  
  return mapping
  
def extract_functions(objectfile):
  cmd = ['gdb', '-batch', objectfile, '-ex', 'info functions']
  output = subprocess.check_output(cmd).strip()
  lines = output.split("\n")
  current_file = '(unknown)'
  object_functions = []
  for i in range(len(lines)):
      line = lines[i].strip()
      if not len(line):
          continue
      if line == "All defined functions:":
          continue
      if line.startswith("File "):
          current_file = line[len("File "):-1]
          continue
      if line.startswith("Non-debugging symbols:"):
        break
      # everything else should now be in the format return name(type1, type2...)
      signature = line
      name = re.split("\(", line)[0].split()[-1]
      while name.startswith("*"):
        name = name[1:]
      object_functions.append((name, current_file, signature))

  object_fns = []
  if not len(object_functions):
    logging.warning("no functions in %s" % (objectfile))
    return []    
  
  function_name_map = map_symbols_to_api_functions(objectfile)
  all_function_names = [of[0] for of in object_functions]
  all_disassemblies = extract_disassemblies(objectfile, all_function_names)
  for fn_info in object_functions:
    function_name = fn_info[0]
    if function_name not in all_disassemblies:
      logging.error("No disassembly for function %s" % (fn_info[0]))
      continue

    function_names = []
    if function_name not in function_name_map:
      logging.error("gdb reported a function %s, but objdump did not" % function_name)
      continue

    sourcefile = fn_info[1]
    signature = fn_info[2]
    
    # TODO: Hash of the database should NOT include the
    # function name, only return type and parameters!!!
    for function_name_canonical in function_name_map[function_name]:
      # Check whether it's safe to replace function
      sig_new = replace_function_name(signature, function_name, function_name_canonical)
      if not sig_new:
        logging.error("could not replace %s with %s in %s" % (function_name, function_name_canonical, signature))
        continue
      # TODO TODO TODO replace(function_name, "")???
      fn = Fn(function_name_canonical, signature, sourcefile)
      fn.disassembly = all_disassemblies[function_name]
      object_fns.append(fn)
  return object_fns

def process_file(fdb, filename, force=False, silent_errors = False):
  filename = os.path.abspath(filename)
  if not is_elf(filename) and not force:
    return None

  logging.debug("processing %s" % filename)
  object_info = ObjectInfo(filename, None, None)

  if not fdb.needs_update(filename):
    if not silent_errors:
      logging.warning("doesn't need update: %s" % filename)
    return None

  object_functions = extract_functions(filename)
  for function in object_functions:
    object_info.add_function(function)

  fdb.store_object(object_info)

  return object_functions

def process_dir(fdb, dirname, maxn=1000):
  i = 0
  new_functions = []
  dirname = os.path.abspath(dirname)
  for f in os.listdir(dirname):
    if i > maxn:
      break

    f_path = os.path.join(dirname, f)
    if os.path.isdir(f_path):
      new_functions_, i_ = process_dir(fdb, f_path, maxn-i)
      i += i_
      new_functions += new_functions_
      continue
    
    object_functions = process_file(fdb, f_path, False, True)
    if object_functions is None:
      continue

    new_functions += object_functions
    i += 1

  return new_functions, i

def main():
  logging.basicConfig(level=logging.INFO)
  fdb = DB()
  new_functions = []
  if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
      if os.path.isdir(arg):
        new_functions += process_dir(fdb, arg)[0]
      elif os.path.isfile(arg):
        file_functions = process_file(fdb, arg, False, True)
        if file_functions is not None:
          new_functions += file_functions
      else:
        logging.error("i don't know what to do with argument %s")
  else:
    new_functions = process_dir(fdb, ".", 400)

  logging.info("scanning finished. found %d new functions. saving" % len(new_functions))


  fdb.save()

if __name__ == "__main__":
  main()
