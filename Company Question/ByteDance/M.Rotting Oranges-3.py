from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        nFresh = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == 1)
        q = deque([(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2])
        while q and nFresh > 0:
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        nFresh -= 1
        return res if nFresh == 0 else -1