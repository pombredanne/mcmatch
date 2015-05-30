#!/usr/bin/python2
import os
import subprocess
from mcmatch.extraction import process_dir

def bash_array_to_els(line):
  try:
    ret = []
    tokens = line.split()
    # sanitize
    for tk in tokens:
      if len(tk) <= 2:
        continue
      if tk[0] == '(':
        tk = tk[1:]
      if tk[0] == '\'':
        tk = tk[1:]
      if tk[-1] == ')':
        tk = tk[:-1]
      if tk[-1] == '\'':
        tk = tk[:-1]
      ret.append(tk)
  except:
    print "Unable to parse line: %s" % line
    raise
  return ret

def els_to_bash_array(els):
  zz = []
  for el in els:
    if ' ' in el:
      zz.append('\'%s\'' % el)
    else:
      zz.append(el)
  return "(" + " ".join(zz) + ")"

def set_debug_options(els):
  if "!debug" in els:
    els.remove('!debug')
  if "strip" in els:
    els.remove("strip")
  if not "!strip" in els:
    els.append('!strip')
  if not "debug" in els:
    els.append("debug")
  return els

def edit_pkgbuild(fname):
  f = open(fname, 'r')
  lines = []
  options = None
  for line in f:
    line = line.strip()
    if line.startswith("options"):
      options = bash_array_to_els(line[line.find("=")+1:].strip())
      options = set_debug_options(options)
    else:
      lines.append(line)

  if options is None:
    options = set_debug_options([])
  f = open(fname, 'w')
  for line in lines:
    if not line.startswith("#") and options is not None:
      f.write('options=' +els_to_bash_array(options) + "\n")
      options = None
    f.write(line + "\n")

def build(path):
  os.chdir(path)
  if not os.path.isfile('PKGBUILD'):
    raise Exception("%s does not contain a PKBUILD" % path)
  subprocess.call('makepkg')

  if not os.path.isdir('pkg'):
    raise Exception("makepkg did not create a 'pkg' directory")

packages = ['git', 'zlib', 'glibc']

def parse_archlinux_dir(d):
  data = {}
  #for filename in os.listdir(d):
  for filename in packages:
    path = ps.path.join(d, filename, 'trunk')
    if os.path.isdir(filepath):
      build(path)
    else:
      raise Exception("ERROR: No such file: %s" %  path)

parse_archlinux_dir(os.getcwd())

