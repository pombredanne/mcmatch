"""
commandline - command line utilities for argument parsing and output.
"""

from mcmatch.metric.counter import counter_metrics
from mcmatch.metric.aggregator import MetricAggregator

class MetricArg(object):
  @staticmethod
  def apply(parser):
      parser.add_argument('-m', '--metric', dest='metrics', action='append', default = [],
          help='use the given metrics', choices=counter_metrics.keys() + ['all'], required=True)
      parser.add_argument('-s', '--scale', dest='scale', action='store_true',
          help='use feature scaling')

  @staticmethod
  def validate(args):
    pass

  @staticmethod
  def get_aggregator(args):
    mtr_instances = []
    if 'all' in args.metrics:
      mtr_instances = [counter_metrics.values()]
    else:
      for m in args.metrics:
        mtr_instances.append(counter_metrics[m])
    return MetricAggregator(mtr_instances)

  @staticmethod
  def scale_features(args):
    return args.scale

