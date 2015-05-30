#!/usr/bin/python2
'''
Created on Jan 6, 2015

@author: niko
'''

import sys
import logging
import argparse
from mcmatch.db.types import Codeblock
from mcmatch.commandline import FeatureArg
from mcmatch.analyze import KNearestNeighbors
from mcmatch.db.pg_database import PgFunDB

def knn_file(fname, fdb, knn):
  assert isinstance(knn, KNearestNeighbors)
  assert isinstance(fdb, PgFunDB)

  f = open(fname, 'r')

  c = Codeblock()
  c.disassembly = map(str.strip, f.readlines())

  distances, function_text_ids = knn.get_neighbours(c)

  # cache compileroptions for all loaded functions
  # TODO
  #fdb.get_objects(function_ids)

  for i in range(0, len(distances[0])):
    function_text_id = function_text_ids[i]
    functions = list(fdb.get_functions_with_textid(function_text_id, include_disassembly=True))
    if not len(functions):
      logging.error("database problem: could not find associated function for fid=%d" % function_id)
      continue
    for function in functions: 
      print distances[0][i], function.get_shortinfo(db=fdb)

def main():
  logging.basicConfig(level=logging.INFO)

  parser = argparse.ArgumentParser(description='find k-nearest-neighbours')
  parser.add_argument('-F', '--file', dest='file', action='append', default = [],
      help='use the given assembly file[s]')
  FeatureArg.apply(parser)
  args = parser.parse_args()
  
  if len(args.file) == 0:
    print "Error: need at least one file."
    return
  
  fdb = PgFunDB()
  metr = FeatureArg.get_aggregator(args)
  scale_features = FeatureArg.scale_features(args)
  knn = KNearestNeighbors(fdb, metr, 30, scale_features=scale_features)
  # TODO Cluster class should accept more than one Codeblock
  for f in args.file:
    knn_file(f, fdb, knn)

if __name__ == '__main__':
  main()
