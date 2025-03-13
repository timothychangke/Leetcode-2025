from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        def bfs(i, j):
            q = deque([i, j])
            v = set()
            depth = 1
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for nr, nc in [(r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)]:
                        if nr in range(ROWS) and nc in range(COLS) and rooms[nr][nc] >= 0:
                            if rooms[nr][nc] == 0:
                                rooms[nr][nc] = depth
                            else:
                                rooms[nr][nc] = min(rooms[nr][nc], depth)
                depth += 1 
        
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    bfs(i, j)
        
