from immutable.immutable import HashMap


class Set(object):
    def __init__(self, size=0):
        self.data = []
        self.__curr__ = 0
        self.hashmap = HashMap(size)

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


def monoid_add(set_1, set_2):
    if len(set_1.data) == 0:
        return set_2
    if len(set_2.data) == 0:
        return set_1
    new_list = set_1.data + set_2.data
    new_list.sort()
    res = Set(size(set_1) + size(set_2))
    for i in new_list:
        if not has(res, i):
            res = add(res, i)
    return res
