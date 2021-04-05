from immutable import HashMap

class Set(object):
  def __init__(self, size):
    self.data = []
    self.hashmap = HashMap(size)

  def __iter__(self):
    return self

  def __next__(self):
    return self.hashmap.__iter__()

def add(aset, value):
  if not type(value) == int or aset.hashmap.has(value):
    return False
  data = aset.data.copy()
  data.append(value)
  res = Set(aset.hashmap.size() + 1)
  res.data = data
  for i in data:
    res.hashmap.add(i)
  return res

def remove(aset, value):
  if not type(value) == int or not aset.hashmap.has(value):
    return False
  data = aset.data.copy()
  new_data = []
  res = Set(aset.hashmap.size() - 1)
  for i in data:
    if not i == value:
      new_data.append(i)
      res.add(i)
  res.data = new_data
  return res

def size(aset):
  return aset.hashmap.size()

def from_list(alist):
  res = Set(len(alist))
  for i in alist:
    if not res.hashmap.has(i):
      res.data.append(i)
      res.hashmap.add(i)
  return res

def to_list(aset):
  return aset.data.copy()

def has(aset, value):
  if not type(value) == int:
    return False
  return aset.hashmap.has(value)

def set_filter(aset, func):
  return aset.hashmap.filter(func)

def set_map(aset, func):
  return aset.hashmap.map(func)

def set_reduce(aset, func, initial):
  return aset.hashmap.hash_reduce(func, initial)