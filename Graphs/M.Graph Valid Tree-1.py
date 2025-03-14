class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        v = set()
        def dfs(i, prev):
            if i in v: return False
            v.add(i)
            for nei in graph[i]:
                if nei != prev:
                    if not dfs(nei, i): return False
            return True
        return dfs(0, -1) and len(v) == n