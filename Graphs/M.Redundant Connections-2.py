class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x):
        res = x
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b: return False
        if self.rank[a] > self.rank[b]:
            self.rank[a] += self.rank[b]
            self.par[b] = a
        else:
            self.rank[b] += self.rank[a]
            self.par[a] = b
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for a, b in edges:
            if not uf.union(a, b): return [a, b]
            