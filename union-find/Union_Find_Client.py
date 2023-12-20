from QuickFind_UnionFind import *

input = [[0,2], [1,4]]
quick_find = QuickFind_UnionFind(3)

for item in input:
    p = item[0]
    q = item[1]
    if not quick_find.connected(p, q):
        quick_find.union(p, q)

print(quick_find)