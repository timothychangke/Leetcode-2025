from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        q = deque([(r, c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0])
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()               
                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if nr in range(rows) and nc in range(cols) and rooms[nr][nc] == 2**31 - 1:
                        rooms[nr][nc] = rooms[r][c] + 1
                        q.append((nr, nc)) 