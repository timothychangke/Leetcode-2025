class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        def find(x):
            res = x
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(x, y):
            a, b = find(x), find(y)
            if a == b: return False
            if rank[a] > rank[b]:
                rank[a] += rank[b]
                par[b] = a
            else:
                rank[b] += rank[a]
                par[a] = b
            return True
        res = [-1, -1]
        for a, b in edges:
            if not union(a, b): res = [a,b]
        return res