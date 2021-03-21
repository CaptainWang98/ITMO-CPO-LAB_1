class HashMap(object):
  def __init__(self, size = 0):
    self.__curr__ = 0
    self.len = 0
    self.data = []
    self.allocate_memory(size)

  def allocate_memory(self, size):
    # define new properties
    new_data = []
    new_len = self.len + size
    for i in range(new_len):
      new_data.append(None)
    # rehash
    for i in self.data:
      index = i % new_len
      if not (i == None):
        if new_data[index] == None:
          new_data[index] = i
        else:
          flag = True
          while flag:
            index += 1
            if new_data[index] == None:
              new_data[index] = i
            flag = False
    # set new properties
    self.data = new_data
    self.len = new_len

    def __iter__(self):
      return self

    def __next__(self):
      if self.size > 0:
        if self.__curr__ < self.size:
          tmp = self.data[self.__curr__]
          self.__curr__ += 1
          return tmp
        else:
          self.__curr__ = 0
          raise StopIteration
      else:
        raise StopIteration

def add(hashmap, value):
  if not type(value) == int:
    return False
  index = value % hashmap.len
  if hashmap.data[index] == None:
    hashmap.data[index] = value
  else:
    # collision resolution: open address
    flag = True
    # search a None place
    while flag and index < hashmap.len:
      if (hashmap.data[index] == None):
        hashmap.data[index] = value
        flag = False
      index += 1
    # can not find, then allocate memory and store new value
    if flag and (index >= hashmap.len):
      hashmap.allocate_memory(hashmap.len)
      add(hashmap, value)

def remove(hashmap, value):
  if not type(value) == int:
    return False
  index = value % hashmap.len
  if (hashmap.data[index] == value):
    hashmap.data[index] = None
    return True
  else:
    flag = True
    while flag and (index < hashmap.len):
      if hashmap.data[index] == value:
        hashmap.data[index] = None
        return True
      index += 1
    return False

def size(hashmap):
  return hashmap.len

def from_list(hashmap, alist):
  if not type(alist) == list:
    return False
  for i in alist:
    add(hashmap, i)


def to_list(hashmap):
  return hashmap.data[:]

def find(hashmap, value):
  index = value % hashmap.len
  while index < hashmap.len:
    if hashmap.data[index] == value:
      return True
    index += 1
  return False

def filter(hashmap, func):
  res = []
  for i in hashmap.data:
    if func(i):
      res.append(i)
  return res


def map(hashmap, func):
  res = []
  for i in hashmap.data:
    res.append(func(i))
  return res

def hash_reduce(hashmap, func, initial):
  accumulator = initial
  for i in hashmap.data:
    accumulator = func(accumulator, i)
  return accumulator

