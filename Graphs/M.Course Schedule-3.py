from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            degree[a] += 1
        q = deque([i for i, d in enumerate(degree) if not d])
        c = 0
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                c += 1
                for nei in g[course]:
                    degree[nei] -= 1
                    if not degree[nei]:
                        q.append(nei)
        return c == numCourses