import unittest
from hypothesis import given, note, strategies as st
import sys
sys.path.append("/Users/cptw98/Desktop/CPO/ITMO-CPO-LAB_1/src/mutable")
from mutable_set import Set

class TestMutableSet(unittest.TestCase):
  def setUp(self):
    self.set = Set(3)

  def tearDown(self):
    self.set = None
    del self.set

class TestMutableSetMethods(TestMutableSet):
  def test_init(self):
    self.assertEqual(self.set.size(), 3)
    self.assertIsInstance(self.set.data, list)
    self.assertEqual(len(self.set.data), 0)

  @unittest.expectedFailure
  def test_init_fail(self):
    self.assertEqual(self.set.data[1], None)

  def test_add(self):
    for i in range(5):
      self.set.add(i)
    self.assertEqual(self.set.data[0], 0)
    self.assertEqual(self.set.data[1], 1)
    self.assertEqual(self.set.data[2], 2)
    self.assertEqual(self.set.data[3], 3)
    self.assertEqual(self.set.data[4], 4)
    self.assertEqual(self.set.add("String"), False)

  def test_remove(self):
    self.set.add(0)
    self.assertEqual(self.set.data[0], 0)
    self.assertEqual(self.set.size(), 3)
    self.set.remove(0)
    self.assertEqual(self.set.size(), 3)
    self.assertEqual(self.set.remove("String"), False)

  def test_size(self):
    self.assertEqual(self.set.size(), 3)

  def test_from_list(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set.from_list(alist)
    self.assertEqual(self.set.data[0], 0)
    self.assertEqual(self.set.data[1], 1)
    self.assertEqual(self.set.data[2], 2)
    self.assertEqual(self.set.data[3], 3)
    self.assertEqual(self.set.data[4], 4)
    self.assertEqual(self.set.data[5], 11)
  
  def test_to_list(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set.from_list(alist)
    self.assertEqual(self.set.to_list(), alist)
    self.assertEqual(self.set.size(), 6)

  def test_has(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set.from_list(alist)
    self.assertEqual(self.set.has(11), True)
    self.assertEqual(self.set.has(9), False)

  def test_filter(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set.from_list(alist)

    def filterOdd(value):
      if value % 2 == 0:
        return True
      else:
        return False

    res = self.set.filter(filterOdd)
    for i in res:
      self.assertEqual((i == 0) or (i == 2) or (i == 4), True)
    self.assertEqual(len(res), 3)
    

  def test_map(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set.from_list(alist)

    def mapPlusOne(value):
      return value + 1

    res = self.set.map(mapPlusOne)
    self.assertEqual(res, [1, 2, 3, 4, 5, 12])

  def test_reduce(self):
    alist = [0, 1, 2, 3, 4, 11]
    self.set.from_list(alist)

    def reduceSum(accumulator, curr):
      return accumulator + curr

    res = self.set.set_reduce(reduceSum, 0)
    self.assertEqual(res, 21)

  @given(st.lists(st.integers(), max_size=10))
  def test_from_list_equals_to_list(self, alist):
    new_list = []
    for i in alist:
      if not i in new_list:
        new_list.append(i)
    aset = Set(3)
    aset.from_list(alist)
    self.assertEqual(aset.to_list(), new_list)

  @given(st.lists(st.integers(), max_size=10))
  def test_iter(self, alist):
    aset = Set(3)
    new_list = []
    for i in alist:
      if not i in new_list:
        new_list.append(i)
    aset.from_list(alist)
    equal_new_list = []
    for i in aset:
      equal_new_list.append(i)
    self.assertEqual(new_list, equal_new_list)

  @given(st.lists(st.integers(), max_size=10))
  def test_moid_identity(self, alist):
    identity_set = Set()
    aset = Set(3)
    aset.from_list(alist)
    aset.monoid_add(identity_set)
    new_list = []
    for i in alist:
      if not i in new_list:
        new_list.append(i)
    self.assertEqual(aset.data, new_list)

if __name__ == '__main__':
  unittest.main()