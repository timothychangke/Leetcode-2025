from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        leaves_q = deque([i for i, arr in enumerate(adj) if len(arr) == 1])
        while n > 2:
            n -= len(leaves_q)
            for _ in range(len(leaves_q)):
                i = leaves_q.popleft()
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    leaves_q.append(j)
        return list(leaves_q)
        
        
        
        
""" 
The idea is to identify the leave nodes, then traverse closer and closer to the center. Like a bfs but from the end of the graph
The condition will terminate once at most 2 MHT roots are found, there can never be 3 as the either 1. it is a cycle or 2. the center node is deeper than the other two nodes
"""