from mcmatch.db.pg_database import PgFunDB as DB
import logging
import argparse

from mcmatch.metric.counter import counter_metrics

def main():
  available_metrics = counter_metrics.keys()
  logging.basicConfig(level=logging.INFO)

  parser = argparse.ArgumentParser(description='perform delete actions between functions in the database')
  parser.add_argument('-o', '--object', dest='objects', action='append', default = [],
      help='delete objects by full path', required=True)
  args = parser.parse_args()

  fundb = DB()
  for obj in args.objects:
    logging.info("deleting %s" % obj)
    fundb.delete_objects_by_filename(obj)
  fundb.save()

if __name__ == "__main__":
  main()
