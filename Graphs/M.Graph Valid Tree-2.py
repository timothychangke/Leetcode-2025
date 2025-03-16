class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[] for i in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        v = set()
        def dfs(i, prev):
            if i in v: return False 
            v.add(i)
            for nei in g[i]:
                if nei != prev:
                    if not dfs(nei, i): return False
            return True
        return dfs(0, -1) and len(v) == n
