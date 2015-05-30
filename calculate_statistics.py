#!/usr/bin/python2
from mcmatch.db.pg_database import PgFunDB as DB
#from mcmatch.metric.counter import counter_metrics
from mcmatch.metric import all_metrics
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
  parser.add_argument('-X', '--recreate-tables', help='recreate all metric tables and exit',
      action='store_true', dest='recreate_tables')
  parser.add_argument('-m', '--metric', dest='metric', choices=all_metrics.keys(), nargs='*')
  args = parser.parse_args()

  fundb = DB()

  match_metrics = []
  for mtr in all_metrics:
    if args.metric is not None and len(args.metric) and not mtr in args.metric:
      continue
    match_metrics.append(mtr)

  if args.recreate_tables:
    for m in match_metrics:
      logging.info("recreating table for metric %s" % m)
      fundb.recreate_metrics_table(all_metrics[m])
    fundb.save()
    return
  
  if args.force:
    for m in match_metrics:
      logging.info("clearing data for feature %s" % m)
      fundb.delete_feature_data(all_metrics[m])
  
  logging.info("looking for missing metrics")
  function_texts = fundb.get_function_texts(with_missing_metrics=[all_metrics[m] for m in match_metrics])

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
    
    logging.debug("updating metrics for %d/%s..." % (text_id, signature))
    for m in all_metrics:
      mcounter = all_metrics[m]
      mcounter.calculate(c)
      fundb.store_metrics(text_id, mcounter)
    fundb.save()
    
  fundb.save()

  

if __name__ == "__main__":
  main()
