from counter import counter_features, counter_sum_features
from length import textlength_features
from mcmatch.feature.counter import relative_counter_features,\
  relative_counter_sum_features
from cyclo import cyclo_feature

all_features = dict(list(counter_features.items())
                   + list(counter_sum_features.items())
                   + list(textlength_features.items())
                   + list(relative_counter_features.items())
                   + list(relative_counter_sum_features.items())
                   + list(cyclo_feature.items()))

grouped_features = {
    'counter' : counter_features,
    'counter_sum' : counter_sum_features,
    'textlength' : textlength_features,
    'relative_counter' : relative_counter_features,
    'relative_counter_sum' : relative_counter_sum_features,
    'control_flow' : cyclo_feature }
