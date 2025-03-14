from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        visited = 0
        res = []
        for a, b in prerequisites:
            g[b].append(a)
            degree[a] += 1
        q = deque([i for i, d in enumerate(degree) if not d])
        while q:
            cur = q.popleft()
            visited += 1
            res.append(cur)
            for nei in g[cur]:
                if not degree[nei]:
                    q.append(nei)
        return res if visited == numCourses else -1