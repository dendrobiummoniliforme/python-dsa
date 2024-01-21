import unittest
from src.UnionFind.WeightedQuickUnion_UnionFind import WeightedQuickUnion_UnionFind

class TestQuickUnion(unittest.TestCase):
    def setUp(self):
        self.quick_union = WeightedQuickUnion_UnionFind(10)
        self.input = [[4,3], [3,8], [6,5], [9,4], [2,1], [5,0], [7,2], [6,1], [7,3]]

    def test_not_connected(self):
        for item in self.input:
            p = item[0]
            q = item[1]
            self.assertEqual(False, self.quick_union.connected(p, q), "SHOULD be false when finding two unrelated ids.")

    def test_union(self):
        for item in self.input:
            self.quick_union.__repr__()
            p = item[0]
            q = item[1]
            if not self.quick_union.connected(p, q):
                self.quick_union.union(p, q)
        self.assertEqual(self.quick_union.__repr__(), "<WeightedQuickUnion_UnionFind id, size:([6, 2, 6, 4, 6, 6, 6, 2, 4, 4], [1, 1, 3, 1, 4, 1, 10, 1, 1, 1])>")
    
    def test_connected(self):
        for item in self.input:
            p = item[0]
            q = item[1]
            if not self.quick_union.connected(p, q):
                self.quick_union.union(p, q)
                self.assertEqual(True, self.quick_union.connected(p, q), "SHOULD be true when finding two related ids.")

if __name__ == '__main__':
    unittest.main()