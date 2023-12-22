import unittest
from UnionFind.QuickUnion_UnionFind import QuickUnion_UnionFind

class TestQuickUnion(unittest.TestCase):
    def test_not_connected(self):
        quick_union = QuickUnion_UnionFind(3)
        input = [[0,2], [1,2]]
        for item in input:
            p = item[0]
            q = item[1]
            self.assertEqual(False, quick_union.connected(p, q), "SHOULD be false when finding two unrelated ids.")

    def test_union(self):
        quick_union = QuickUnion_UnionFind(3)
        input = [[0,2], [1,2]]
        for item in input:
            p = item[0]
            q = item[1]
            if not quick_union.connected(p, q):
                quick_union.union(p, q)
        self.assertEqual(quick_union.__repr__(), "<QuickUnion_UnionFind id:[2, 2, 2]>")
    
    def test_connected(self):
        quick_union = QuickUnion_UnionFind(3)
        input = [[0,2], [1,2]]
        for item in input:
            p = item[0]
            q = item[1]
            if not quick_union.connected(p, q):
                quick_union.union(p, q)
                self.assertEqual(True, quick_union.connected(p, q), "SHOULD be true when finding two related ids.")

if __name__ == '__main__':
    unittest.main()