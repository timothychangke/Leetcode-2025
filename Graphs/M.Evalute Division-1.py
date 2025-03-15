from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for vertices, value in zip(equations, values):
            x, y = vertices
            graph[x].append((y, value))
            graph[y].append((x, 1/value))
        def dfs(x, y, value, visited):
            if x not in graph or y not in graph: return -1
            if x == y: return value
            visited.add(x)
            for nei, v in graph[x]:
                if nei not in visited:
                    res = dfs(nei, y, value * v, visited)
                    if res != -1.0:
                        return res
            return -1.0
        res = []
        for q in queries:
            x, y = q
            res.append(dfs(x, y, 1.0, set()))
        return res