#!/usr/bin/python2
import sys
import os
from mcmatch.db.pg_database import PgFunDB

fdb = PgFunDB()
cmds = {}

def repo(args):
  if not len(args) or args[0] == 'ls':
    rx = fdb.get_repository_names()
    for r in rx:
      print r

cmds['repo'] = repo

def _objfile_objids(args):
  for arg in args:
    arg = os.path.abspath(arg)
    objids = fdb.get_objectids_matching(path_is=arg)
    if not len(objids):
      print "Error: No object matching path %s" % (arg)
      continue
    yield objids

def objfile_show(args):
  for objids in _objfile_objids(args):
    ojects = fdb.get_objects(objids)
    for obj in ojects:
      print obj.get_path(), "(#%d)" % obj.id
      print obj.get_compileopts().get_shortinfo(),
      print obj.get_mtime(),
      if obj.locked:
        print "(Locked)"
      else:
        print "(UnLocked)"
      funs = list(fdb.get_functions_by_objectid(obj.id))
      print len(funs), "functions."

def objfile_lock(args):
  for objids in _objfile_objids(args):
    for objid in objids:
      print "Locking #%d" % objid
      fdb.lock_object(objid)

def objfile(args):
  subcommands = {'show': objfile_show, 'lock' : objfile_lock}
  if not len(args) or not args[0] in subcommands:
    print "objfile subcommands:"
    for cmd in subcommands.keys():
      print cmd
    return
  subcommands[args[0]](args[1:])

cmds['obj'] = objfile

def cleanup(args):
  if len(args):
    print "cleanup does not take any parameters"
    return
  fdb.delete_stale_functiontexts()

cmds['cleanup'] = cleanup

def main():
  sys.argv = sys.argv[1:]
  if not len(sys.argv):
    for c in cmds.keys():
      print c
    return

  a, b = sys.argv[0], sys.argv[1:]
  if a in cmds:
    cmds[a](b)
    fdb.save()
  else:
    print "No such command: %s" % (a)

main()
