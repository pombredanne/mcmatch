'''
Created on Jan 22, 2015

@author: niko
'''

import re
import doctest
import logging


class NN2ProgressPrinter(object):
  """Progress printer for an O(n*(n/2)) algorithm."""
  def __init__(self, n):
    self.n = n
    self.total_ops = n*(n-1)/2
    self.current = 0
    self.last = 0
    self.res = 5

  def bump(self):
    """This function, when called at the beginning of the outer loop, will output the current
    process."""
    percentage = int(float(self.current)/self.total_ops * 100.0)
    if percentage >= self.last + self.res:
      logging.info("processing (%d/%d, %d%% complete)" % (self.current, self.total_ops, percentage))
    self.last = int(percentage / self.res) * self.res
    self.n -= 1
    self.current += self.n

class NProgressPrinter(object):
  def __init__(self, n):
    self.total_ops = n
    self.current = 0
    self.last = 0
    self.res = 5

  def bump(self):
    percentage = int(float(self.current)/self.total_ops * 100.0)
    if percentage >= self.last + self.res:
      logging.info("processing (%d/%d, %d%% complete)" % (self.current, self.total_ops, percentage))
    self.last = int(percentage / self.res) * self.res
    self.current += 1


def extract_funname(sig, full=False):
  """returns the function name from a function signature. The optional
  'full' parameter will extract any meta information encoded into the
  function name as well. Example:
  
  >>> extract_funname('static void xdrrec_destroy(XDR *);')
  'xdrrec_destroy'
  
  >>> extract_funname('key_t ftok(const char *, int);')
  'ftok'
  
  >>> extract_funname('int *__h_errno_location(void);')
  '__h_errno_location'
  
  >>> extract_funname('int sem_destroy@@GLIBC_2.2.5(sem_t *);')
  'sem_destroy'
  
  >>> extract_funname('int sem_destroy@@GLIBC_2.2.5(sem_t *);', True)
  'sem_destroy@@GLIBC_2.2.5'
  
  >>> extract_funname('static void xdrrec_destroy(XDR *);', True)
  'xdrrec_destroy'
  
  >>> extract_funname('int *__h_errno_location(void);', True)
  '__h_errno_location'
  
  """
  m = re.match(r'^.*[^a-zA-Z0-9_]+([a-zA-Z_][a-zA-Z_0-9]*)(@@?[a-zA-Z0-9_\.]+)?\(.+$', sig)
  if not m:
    raise ValueError("Not a function signature: " + sig)
  if full and m.lastindex == 2:
    return m.group(1) + m.group(2)
  return m.group(1)

def signature_to_fname_heuristic(signature):
  f = extract_funname(signature, full=False)
  while len(f) > 1 and f.startswith("_"):
    f = f[1:]
  if f.startswith("GI_"):
    f = f[3:]
  if f.startswith("IO_"):
    f = f[3:]
  while len(f) > 1 and f.startswith("_"):
    f = f[1:]
  return f

def replace_function_name(signature, function_name, function_name_canonical):
  """replace the function name in the signature with the canonical version.
  Returns the updated signature if a replacement was done, None otherwise.
  
  >>> replace_function_name('int sem_destroy@@GLIBC_2.2.5(sem_t *);', 'sem_destroy', 'abc')
  'int abc(sem_t *);'
  
  >>> replace_function_name('void glob(glob *z)', 'glob', 'abc')
  'void abc(glob *z)'
  
  >>> replace_function_name('void globber(glob *z)', 'glob', 'abc') is None
  True
  
  """
  function_name_full = extract_funname(signature, True)
  function_name_stripped = extract_funname(signature, False)
  
  if signature.count(function_name) == 1:
    return signature.replace(function_name_full, function_name_canonical)
  
  if signature.count(function_name) >= 1:
    # if the first match is before the first opening
    # parenthesis:
    if signature.find(function_name) < signature.find("("):
      # run extract-funname on this, check that
      # extract_funname match contains the string, then replace
      # the whole extracted thingy including the @@GLIBC-... part
      # with the canonical name
      if function_name == function_name_stripped:
        return signature.replace(function_name_full, function_name_canonical, 1)
        
  return None

if __name__ == '__main__':
  doctest.testmod()