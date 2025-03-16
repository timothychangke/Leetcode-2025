class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x):
        res = x
        while self.par[res] != res:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res
    def union(self, x, y):
        a, b = self.find(x), self.find(y) 
        if a == b: return 0
        if self.rank[a] > self.rank[b]:
            self.rank[a] += self.rank[b]
            self.par[b] = a
        else:
            self.rank[b] += self.rank[a]
            self.par[a] = b
        return 1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            n -= uf.union(a, b)
        return n
            