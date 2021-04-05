from mutable import HashMap

class Set(object):
  def __init__(self, size):
    self.data = []
    self.hashmap = HashMap(size)
  
  def add(self, value):
    if not type(value) == int:
      return False
    if self.hashmap.has(value):
      return False
    else:
      self.data.append(value)
      self.hashmap.add(value)

  def remove(self, value):
    if not type(value) == int:
      return False
    if self.hashmap.remove(value):
      self.data.remove(value)

  def has(self, value):
    if not type(value) == int:
      return False
    return self.hashmap.has(value)

  def size(self):
    return self.hashmap.size()

  def from_list(self, alist):
    for i in alist:
      if type(i) == int and not self.hashmap.has(i):
        self.data.append(i)
        self.hashmap.add(i)

  def to_list(self):
    return self.data.copy()

  def filter(self, func):
    return self.hashmap.filter(func)

  def map(self, func):
    return self.hashmap.map(func)

  def hash_reduce(self, func, initial):
    return self.hashmap.hash_reduce(func, initial)

  def __iter__(self):
    return self.hashmap

  def __next__(self):
    return self.hashmap.__next__()