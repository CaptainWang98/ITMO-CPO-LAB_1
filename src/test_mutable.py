import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *


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
            self.hashMap.add(i)
        self.assertEqual(self.hashMap.data[0], 0)
        self.assertEqual(self.hashMap.data[1], 1)
        self.assertEqual(self.hashMap.data[2], 2)
        self.assertEqual(self.hashMap.data[3], 3)
        self.assertEqual(self.hashMap.data[4], 4)
        self.assertEqual(self.hashMap.data[5], None)
        self.assertEqual(self.hashMap.add("String"), False)

    def test_remove(self):
        self.hashMap.add(0)
        self.assertEqual(self.hashMap.data[0], 0)
        self.hashMap.remove(0)
        self.assertEqual(self.hashMap.data[0], None)
        self.assertEqual(self.hashMap.remove("String"), False)

    def test_size(self):
        self.assertEqual(self.hashMap.size(), 3)

    def test_from_list(self):
        alist = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(alist)
        self.assertEqual(self.hashMap.data[0], 0)
        self.assertEqual(self.hashMap.data[1], 1)
        self.assertEqual(self.hashMap.data[2], 2)
        self.assertEqual(self.hashMap.data[3], 3)
        self.assertEqual(self.hashMap.data[4], 4)
        self.assertEqual(self.hashMap.data[5], 11)

    def test_to_list(self):
        alist = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(alist)
        self.assertEqual(self.hashMap.to_list(), alist)
        self.assertEqual(self.hashMap.size(), 6)

    def test_has(self):
        alist = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(alist)
        self.assertEqual(self.hashMap.has(11), True)
        self.assertEqual(self.hashMap.has(9), False)

    def test_filter(self):
        alist = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(alist)

        def filterOdd(value):
            if value % 2 == 0:
                return True
            else:
                return False

        res = self.hashMap.filter(filterOdd)
        self.assertEqual(res, [0, 2, 4])

    def test_map(self):
        alist = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(alist)

        def mapPlusOne(value):
            return value + 1

        res = self.hashMap.map(mapPlusOne)
        self.assertEqual(res, [1, 2, 3, 4, 5, 12])

    def test_reduce(self):
        alist = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(alist)

        def reduceSum(accumulator, curr):
            return accumulator + curr

        res = self.hashMap.hash_reduce(reduceSum, 0)
        self.assertEqual(res, 21)


if __name__ == "__main__":
    unittest.main()
