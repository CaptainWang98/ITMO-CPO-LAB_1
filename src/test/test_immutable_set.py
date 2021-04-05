import unittest
from hypothesis import given, note, strategies as st
import sys
sys.path.append("/Users/cptw98/Desktop/CPO/ITMO-CPO-LAB_1/src/immutable")
from immutable_set import Set, add, remove, size, from_list, to_list, has, set_filter, set_map, set_reduce, monoid_add

class TestMutableSet(unittest.TestCase):
  def setUp(self):
    self.set = Set(3)

  def tearDown(self):
    self.set = None
    del self.set

class TestMutableSetMethods(TestMutableSet):
  def test_init(self):
    self.assertEqual(size(self.set), 3)
    self.assertIsInstance(self.set.data, list)
    self.assertEqual(len(self.set.data), 0)

  @unittest.expectedFailure
  def test_init_fail(self):
    self.assertEqual(self.set.data[3], None)

  def test_add(self):
    for i in range(5):
      self.set = add(self.set, i)
    self.assertEqual(has(self.set, 0), True)
    self.assertEqual(has(self.set, 1), True)
    self.assertEqual(has(self.set, 2), True)
    self.assertEqual(has(self.set, 3), True)
    self.assertEqual(has(self.set, 4), True)
    self.assertEqual(has(self.set, 5), False)
    self.assertEqual(add(self.set, "String"), False)

  def test_remove(self):
    self.set = add(self.set, 0)
    self.assertEqual(has(self.set, 0), True)
    self.set = remove(self.set, 0)
    self.assertEqual(has(self.set, 0), False)
    self.assertEqual(remove(self.set, "String"), False)

  def test_size(self):
    self.assertEqual(size(self.set), 3)

  def test_from_list(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set = from_list(alist)
    self.assertEqual(has(self.set, 0), True)
    self.assertEqual(has(self.set, 1), True)
    self.assertEqual(has(self.set, 2), True)
    self.assertEqual(has(self.set, 3), True)
    self.assertEqual(has(self.set, 4), True)
    self.assertEqual(has(self.set, 5), False)
    self.assertEqual(has(self.set, 11), True)
  
  def test_to_list(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set = from_list(alist)
    self.assertEqual(to_list(self.set), alist)
    self.assertEqual(size(self.set), 6)

  def test_has(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set = from_list(alist)
    self.assertEqual(has(self.set, 11), True)
    self.assertEqual(has(self.set, 9), False)

  def test_filter(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set = from_list(alist)

    def filterOdd(value):
      if value % 2 == 0:
        return True
      else:
        return False

    res = set_filter(self.set, filterOdd)
    self.assertEqual(res, [0, 2, 4])

  def test_map(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set = from_list(alist)

    def mapPlusOne(value):
      return value + 1

    res = set_map(self.set, mapPlusOne)
    self.assertEqual(res, [1, 2, 3, 4, 5, 12])

  def test_reduce(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set = from_list(alist)

    def reduceSum(accumulator, curr):
      return accumulator + curr

    res = set_reduce(self.set, reduceSum, 0)
    self.assertEqual(res, 21)

  @given(st.lists(st.integers(), max_size=10))
  def test_from_list_equals_to_list(self, alist):
    new_list = []
    for i in alist:
      if not i in new_list:
        new_list.append(i)
    note(f"Shuffle:{alist!r}")
    self.set = from_list(alist)
    self.assertEqual(to_list(self.set), new_list)

  @given(st.lists(st.integers(), max_size=10))
  def test_iter(self, alist):
    new_list = []
    for i in alist:
      if not i in new_list:
        new_list.append(i)
    self.set = from_list(alist)
    equal_new_list = []
    for i in self.set:
      equal_new_list.append(i)
    self.assertEqual(new_list, equal_new_list)
  
  @given(st.lists(st.integers(), max_size=10), st.lists(st.integers(), max_size=10), st.lists(st.integers(), max_size=10))
  def test_monoid_add(self, list_1, list_2, list_3):
    set_1 = from_list(list_1)
    set_2 = from_list(list_2)
    set_3 = from_list(list_3)
    self.assertEqual(monoid_add(monoid_add(set_1, set_2), set_3).data, monoid_add(set_1, monoid_add(set_2, set_3)).data)

  @given(st.lists(st.integers(), max_size=10))
  def test_moid_identity(self, alist):
    identity_set = Set()
    self.set = from_list(alist)
    new_set = monoid_add(self.set, identity_set)
    self.assertEqual(new_set.data, self.set.data)

if __name__ == '__main__':
  unittest.main()