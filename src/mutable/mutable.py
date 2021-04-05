class HashMap(object):
  def __init__(self, size = 0):
    self.__curr__ = 0
    self.len = 0
    self.data = []
    self.allocate_memory(size)

  '''
  @description:
    when the memory is not enough, use this method to allocate new memory
    rehash old values, and set new length property
  @args:
    size: int
  @return:
    None
  '''
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


  '''
  @description:
    add new value to HashMap, and handle collision
  @args:
    value: int
  @return:
    None
  '''
  def add(self, value):
    if not type(value) == int:
      return False
    index = value % self.len
    if self.data[index] == None:
      self.data[index] = value
    else:
      # collision resolution: open address
      flag = True
      # search a None place
      while flag and index < self.len:
        if (self.data[index] == None):
          self.data[index] = value
          flag = False
        index += 1
      # can not has, then allocate memory and store new value
      if flag and (index >= self.len):
        self.allocate_memory(self.len)
        self.add(value)


  '''
  @description:
    remove existing value from HashMap
  @args:
    value: int
  @return:
    True: if value exits in HashMap
    False: if value does not exit in HashMap
  '''
  def remove(self, value):
    if not type(value) == int:
      return False
    index = value % self.len
    if (self.data[index] == value):
      self.data[index] = None
      return True
    else:
      flag = True
      while flag and (index < self.len):
        if self.data[index] == value:
          self.data[index] = None
          return True
        index += 1
      return False

  '''
  @description:
    get the size of HashMap
  @args:
    None
  @return:
    type: int
  '''
  def size(self):
    return self.len

  '''
  @description:
    reverse a HashMap does not make sence...
  @args:
    None
  @return:
    None
  '''
  def reverse(self):
    pass

  '''
  @description:
    form a HashMap from a list
  @args:
    alist: list
  @return:
    None
  '''
  def from_list(self, alist):
    if not type(alist) == list:
      return False
    for i in alist:
      self.add(i)

  '''
  @description:
    get a list formed by HashMap values
  @args:
    None
  @return:
    type: list
  '''
  def to_list(self):
    return self.data[:]

  '''
  @description:
    has if the HashMap contain the value
  @args:
    value: int
  @return:
    type: Boolean
  '''
  def has(self, value):
    index = value % self.len
    while index < self.len:
      if self.data[index] == value:
        return True
      index += 1
    return False

  '''
  @description:
    get a list fromed by values which meet the conditions
  @args:
    func: function
    @description: a function to test if the item in HashMap meet the conditions
    @args: item-one of the item in HashMap
    @return:
      if item meets the condition, return True
      if it does not meet the condition, return False
      type: Boolean
  @return:
    type: list
  '''
  def filter(self, func):
    res = []
    for i in self.data:
      if func(i):
        res.append(i)
    return res

  '''
  @description:
    get a list formed by items in HashMap which processed by a function
  @args:
    func: function
    @description: a function process each item in HashMap
    @args: item
    @return: Anytype
  @return:
    type: list
  '''
  def map(self, func):
    res = []
    for i in self.data:
      res.append(func(i))
    return res

  '''
  @description:
    process each value in HashMap and return a acculumator
  @args:
    func: function
    initial: AnyType
  @return:
    AnyType
  '''
  def hash_reduce(self, func, initial):
    accumulator = initial
    for i in self.data:
      accumulator = func(accumulator, i)
    return accumulator

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

class Set(object):
  def __init__(self, size):
    self.data = []
    self.hashmap = HashMap(size)
  
  def add(self, value):
    if self.hashmap.has(value):
      return False
    else:
      self.data.append(value)
      self.hashmap.add(value)

  def remove(self, value):
    if self.hashmap.remove(value):
      self.data.remove(value)

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