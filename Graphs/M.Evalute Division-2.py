from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for e, value in zip(equations, values):
            a, b = e
            g[a].append((b, value))
            g[b].append((a, 1/value))
        res = []
        print(g)
        def bfs(start, end):
            if start not in g or end not in g: return -1.0
            q = deque([(start, 1)])
            v = set()
            v.add(start)
            while q:
                for _ in range(len(q)):
                    n, w = q.popleft()
                    if n == end: return w
                    for nn, nw in g[n]:
                        if nn not in v:
                            v.add(nn)
                            q.append((nn, nw * w))
            return -1.0
        for start, end in queries:
            res.append(bfs(start, end))    
        return res
