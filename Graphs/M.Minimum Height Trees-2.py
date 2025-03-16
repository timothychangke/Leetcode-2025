from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        g = [[] for i in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        q = deque([i for i, arr in enumerate(g) if len(arr) == 1])
        while n > 2:
            for _ in range(len(q)):
                n -= 1
                node = q.popleft()
                for nei in g[node]:
                    g[nei].remove(node)
                    if len(g[nei]) == 1:
                        q.append(nei)
        return list(q)
        
                        
        