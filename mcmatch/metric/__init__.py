from counter import counter_metrics, counter_sum_metrics
from length import textlength_metrics
from mcmatch.metric.counter import relative_counter_metrics,\
  relative_counter_sum_metrics
from cyclo import cyclo_metric

all_metrics = dict(list(counter_metrics.items())
                   + list(counter_sum_metrics.items())
                   + list(textlength_metrics.items())
                   + list(relative_counter_metrics.items())
                   + list(relative_counter_sum_metrics.items())
                   + list(cyclo_metric.items()))

grouped_metrics = {
    'counter' : counter_metrics,
    'counter_sum' : counter_sum_metrics,
    'textlength' : textlength_metrics,
    'relative_counter' : relative_counter_metrics,
    'relative_counter_sum' : relative_counter_sum_metrics,
    'control_flow' : cyclo_metric }
