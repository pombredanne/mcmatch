'''
Created on Jan 7, 2015

@author: niko
'''

class CheckBox(object):
  def __init__(self, key, label=None, default=False):
    self.key = key
    if label is None:
      self.label = key
    else:
      self.label = label
    self.value = default
  
  def updateState(self, prefix, query):
    if (prefix+'_'+self.key) in query:
      self.value = True
    else:
      self.value = False
  
  def getHTML(self, prefix):
    key = prefix + "_" + self.key
    ret = "<input type='checkbox' name='%s' id='%s'" % (key, key)
    if self.value:
      ret += " checked='checked'"
    ret += "></input>\n<label for='%s'>%s</label>" % (key, self.label)
    return ret

class Group(object):
  def __init__(self, prefix, label=None):
    self.prefix = prefix
    if label is None:
      self.label = prefix
    else:
      self.label = label
    
    self.elements = []
  
  def add(self, el, vgroup=None):
    if vgroup is None:
      self.elements.append(("", el))
    else:
      self.elements.append((vgroup, el))
    
  def updateState(self, query):
    for el in self.elements:
      el[1].updateState(self.prefix, query)
  
  def getHTML(self):
    els = sorted(self.elements)
    if not len(els):
      return ""
    lastgroup = None
    rows = []
    for el in els:
      if lastgroup != el[0]:
        rows.append("<strong>%s</strong>" % el[0])
        lastgroup = el[0]
      rows.append(el[1].getHTML(self.prefix))
    return "<br />".join(rows)
  
  def k(self, key):
    for el in self.elements:
      if el[1].key == key:
        return el[1]
    raise IndexError("Could not find key " + key)
 
class Form(object):
  def __init__(self):
    self.groups = []
  
  def addGroup(self, group):
    self.groups.append(group)
  
  def updateState(self, query):
    for g in self.groups:
      g.updateState(query)
  
  def getHTML(self):
    ret = ""
    for g in self.groups:
      ret += "<div class='option_group' id='option_group_%s'><i>%s</i><br />" % (g.prefix, g.label)
      ret += g.getHTML()
      ret += "</div>"
    return ret
  
  def g(self, prefix):
    for g in self.groups:
      if g.prefix == prefix:
        return g
    raise IndexError("Could not find option group " + prefix)
