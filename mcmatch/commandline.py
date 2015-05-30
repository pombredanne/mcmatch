"""
commandline - command line utilities for argument parsing and output.
"""

from mcmatch.feature.counter import counter_features
from mcmatch.feature.aggregator import FeatureAggregator

class FeatureArg(object):
  @staticmethod
  def apply(parser):
      parser.add_argument('-m', '--feature', dest='features', action='append', default = [],
          help='use the given features', choices=counter_features.keys() + ['all'], required=True)
      parser.add_argument('-s', '--scale', dest='scale', action='store_true',
          help='use feature scaling')

  @staticmethod
  def validate(args):
    pass

  @staticmethod
  def get_aggregator(args):
    mtr_instances = []
    if 'all' in args.features:
      mtr_instances = [counter_features.values()]
    else:
      for m in args.features:
        mtr_instances.append(counter_features[m])
    return FeatureAggregator(mtr_instances)

  @staticmethod
  def scale_features(args):
    return args.scale

