from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead: return -1
        if target == "0000": return 0
        steps = 0
        q = deque(["0000"])
        visited = set()
        def neighbours(num):
            res = []
            for i in range(len(num)):
                for x in (1, -1):
                    new_num = num[:i] + str((int(num[i]) + x + 10) % 10) + num[i + 1:]
                    if new_num not in dead and new_num not in visited:
                        res.append(new_num)
            return res
        while q:
            steps += 1
            for _ in range(len(q)):
                num = q.popleft()
                for nei in neighbours(num):
                    if nei == target:
                        return steps
                    q.append(nei)
                    visited.add(nei)
        return -1
