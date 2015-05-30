#!/usr/bin/python2
from mcmatch.db.pg_database import PgFunDB as DB
#from mcmatch.feature.counter import counter_features
from mcmatch.feature import all_features
from mcmatch.util import NProgressPrinter
import logging
import re
import sys
import argparse
import pprint
from mcmatch.db.types import Codeblock

def main():
  logging.basicConfig(level=logging.INFO)
  
  parser = argparse.ArgumentParser(description='perform diff actions between functions in the database')
  #parser.add_argument('-o', '--objects', dest='object_filter', action='append', default = [],
  #    help='only process functions in objects whose name contains this parameter. Can be specified multiple times to match name against any of the list.')
  parser.add_argument('-x', '--force', dest='force', help='clear all statistics', action="store_true")
  parser.add_argument('-X', '--recreate-tables', help='recreate all feature tables and exit',
      action='store_true', dest='recreate_tables')
  parser.add_argument('-m', '--feature', dest='feature', choices=all_features.keys(), nargs='*')
  args = parser.parse_args()

  fundb = DB()

  match_features = []
  for mtr in all_features:
    if args.feature is not None and len(args.feature) and not mtr in args.feature:
      continue
    match_features.append(mtr)

  if args.recreate_tables:
    for m in match_features:
      logging.info("recreating table for feature %s" % m)
      fundb.recreate_features_table(all_features[m])
    fundb.save()
    return
  
  if args.force:
    for m in match_features:
      logging.info("clearing data for feature %s" % m)
      fundb.delete_feature_data(all_features[m])
  
  logging.info("looking for missing features")
  function_texts = fundb.get_function_texts(with_missing_features=[all_features[m] for m in match_features])

  if len(function_texts) == 0:
    logging.warning("seems like everything is already up-to-date.")
    return
  logging.info("done, starting calculations")

  
  prog = NProgressPrinter(len(function_texts))
  for row in function_texts:
    prog.bump()
    text_id, signature, text = row
    
    c = Codeblock()
    c.disassembly_from_text(text)
    
    logging.debug("updating features for %d/%s..." % (text_id, signature))
    for m in all_features:
      mcounter = all_features[m]
      mcounter.calculate(c)
      fundb.store_features(text_id, mcounter)
    fundb.save()
    
  fundb.save()

  

if __name__ == "__main__":
  main()
