class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(i):
            res = i
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(x, y):
            a, b = find(x), find(y)
            if a == b: return 0
            if rank[a] > rank[b]:
                rank[a] += rank[b]
                par[b] = a
            else:
                rank[b] += rank[a]
                par[a] = b
            return 1
        res = n
        for x, y in edges:
            res -= union(x, y)
        return res
                