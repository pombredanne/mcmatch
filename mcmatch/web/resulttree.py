'''
Created on Jan 13, 2015

@author: niko
'''

import logging
import random

class FunctionTextTree(object):
  def __init__(self, fdb, function_text_id, cache_containers=True):
    self.function_text_id = function_text_id
    self.fdb = fdb

    self.cache_containers()

  @staticmethod
  def _unique_id(prefix="ftt", parent=1):
    return "mxmatch_%s_%s_%d" % (prefix, str(parent), random.randint(0, 0xffffffff))

  def cache_containers(self):
    self.functions = list(self.fdb.get_functions_with_textid(self.function_text_id))
    if not len(self.functions):
      logging.error("database problem: could not find associated function for fid=%d" % self.function_text_id)
      self.functions = []

  def get_html(self):
    if not len(self.functions):
      return "(unknown function text %d, potentially database inconsistency/stale data)" % self.function_text_id

    sublist_id = self._unique_id(parent=self.function_text_id)

    ret = self.functions[0].get_shortinfo_html(db=self.fdb)
    if len(self.functions)>1:
      ret += " +<a href='javascript:void(0)' onclick='toggle_visibility(\"%s\");'>%d more</a>:" % (sublist_id, len(self.functions)-1)

      ret += "<div><ul id='%s' style='display: none'>" % sublist_id
      for fn in self.functions[1:]:
        ret += "<li>" + fn.get_shortinfo_html(db=self.fdb) + "</li>"
      ret += "</div></span>"
    else:
      ret += "<br />"

    return ret
