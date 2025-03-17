from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        nFresh = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == 1)
        rotten = deque([(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2])
        time = 0
        while rotten and nFresh > 0:
            time += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        nFresh -= 1
                        rotten.append((nr, nc))
        return time if nFresh == 0 else -1

        