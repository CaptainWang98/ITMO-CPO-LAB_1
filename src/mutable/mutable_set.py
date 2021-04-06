from mutable.mutable import HashMap


class Set(object):
    def __init__(self, size=0):
        self.data = []
        self.__curr__ = 0
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
        # self.data = []
        if len(alist) == 0:
            return
        for i in alist:
            if not self.hashmap.has(i):
                self.data.append(i)
                self.hashmap.add(i)

    def to_list(self):
        return self.data.copy()

    def filter(self, func):
        return self.hashmap.filter(func)

    def map(self, func):
        return self.hashmap.map(func)

    def set_reduce(self, func, initial):
        return self.hashmap.hash_reduce(func, initial)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) > 0:
            if self.__curr__ < len(self.data):
                tmp = self.data[self.__curr__]
                self.__curr__ += 1
                return tmp
            else:
                self.__curr__ = 0
                raise StopIteration
        else:
            raise StopIteration

    def monoid_add(self, set_2):
        # if len(self.data) == 0:
        #   return set_2
        if len(set_2.data) == 0:
            return
        for i in set_2.data:
            if not self.has(i):
                self.data.append(i)
                self.hashmap.add(i)
