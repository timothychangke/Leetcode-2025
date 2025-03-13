from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == 0: return -1
        fresh_num = sum(1 for i in range(ROWS) for j in range(COLS) if grid[i][j] == 1)
        rotten = deque([(i, j) for i in range(ROWS) for j in range(COLS) if grid[i][j] == 2])
        minutes = 0
        while rotten and fresh_num > 0:
            minutes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for nr, nc in (r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1):
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))
                        fresh_num -= 1
        return minutes if fresh_num == 0 else -1
                        
            