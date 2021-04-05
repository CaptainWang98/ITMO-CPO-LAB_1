import unittest
from hypothesis import given
import hypothesis.strategies as st
import sys
sys.path.append("/Users/cptw98/Desktop/CPO/ITMO-CPO-LAB_1/src/immutable")
from immutable import *

class TestMutableHashMap(unittest.TestCase):
  def setUp(self):
    self.hashMap = HashMap(3)

  def tearDown(self):
    self.hashMap = None
    del self.hashMap

class TestMutableHashMapMethods(TestMutableHashMap):
  def test_init(self):
    self.assertEqual(self.hashMap.len, 3)
    self.assertIsInstance(self.hashMap.data, list)
    self.assertEqual(self.hashMap.data[0], None)
    self.assertEqual(self.hashMap.data[1], None)
    self.assertEqual(self.hashMap.data[2], None)

  @unittest.expectedFailure
  def test_init_fail(self):
    self.assertEqual(self.hashMap.data[3], None)

  def test_add(self):
    for i in range(5):
      add(self.hashMap, i)
    self.assertEqual(self.hashMap.data[0], 0)
    self.assertEqual(self.hashMap.data[1], 1)
    self.assertEqual(self.hashMap.data[2], 2)
    self.assertEqual(self.hashMap.data[3], 3)
    self.assertEqual(self.hashMap.data[4], 4)
    self.assertEqual(self.hashMap.data[5], None)
    self.assertEqual(add(self.hashMap, "String"), False)

  def test_remove(self):
    add(self.hashMap, 0)
    self.assertEqual(self.hashMap.data[0], 0)
    remove(self.hashMap, 0)
    self.assertEqual(self.hashMap.data[0], None)
    self.assertEqual(remove(self.hashMap, "String"), False)

  def test_size(self):
    self.assertEqual(size(self.hashMap), 3)

  def test_from_list(self):
    alist = [0, 1, 2, 3, 4, 11]
    from_list(self.hashMap, alist)
    self.assertEqual(self.hashMap.data[0], 0)
    self.assertEqual(self.hashMap.data[1], 1)
    self.assertEqual(self.hashMap.data[2], 2)
    self.assertEqual(self.hashMap.data[3], 3)
    self.assertEqual(self.hashMap.data[4], 4)
    self.assertEqual(self.hashMap.data[5], 11)
  
  def test_to_list(self):
    alist = [0, 1, 2, 3, 4, 11]
    from_list(self.hashMap, alist)
    self.assertEqual(to_list(self.hashMap), alist)
    self.assertEqual(size(self.hashMap), 6)

  def test_has(self):
    alist = [0, 1, 2, 3, 4, 11]
    from_list(self.hashMap, alist)
    self.assertEqual(has(self.hashMap, 11), True)
    self.assertEqual(has(self.hashMap, 9), False)

  def test_filter(self):
    alist = [0, 1, 2, 3, 4, 11]
    from_list(self.hashMap, alist)

    def filterOdd(value):
      if value % 2 == 0:
        return True
      else:
        return False

    res = filter(self.hashMap, filterOdd)
    self.assertEqual(res, [0, 2, 4])

  def test_map(self):
    alist = [0, 1, 2, 3, 4, 11]
    from_list(self.hashMap, alist)

    def mapPlusOne(value):
      return value + 1

    res = map(self.hashMap, mapPlusOne)
    self.assertEqual(res, [1, 2, 3, 4, 5, 12])

  def test_reduce(self):
    alist = [0, 1, 2, 3, 4, 11]
    from_list(self.hashMap, alist)

    def reduceSum(accumulator, curr):
      return accumulator + curr

    res = hash_reduce(self.hashMap, reduceSum, 0)
    self.assertEqual(res, 21)

if __name__ == '__main__':
  unittest.main()