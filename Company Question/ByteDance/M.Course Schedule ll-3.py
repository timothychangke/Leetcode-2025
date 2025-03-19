from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        g = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for a, b in prerequisites:
            degree[a] += 1
            g[b].append(a)
        q = deque([i for i, n in enumerate(degree) if not n])
        while q:
            n = q.popleft()
            res.append(n)
            for nei in g[n]:
                degree[nei] -= 1
                if not degree[nei]:
                    q.append(nei)
        return res if len(res) == numCourses else []
            