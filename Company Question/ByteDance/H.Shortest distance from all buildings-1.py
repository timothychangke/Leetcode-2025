from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        g = [[0 for _ in range(cols)] for _ in range(rows)]
        empty = 0
        res = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    local_min = float('inf')
                    q = deque([(r, c, 0)])
                    while q:
                        for _ in range(len(q)):
                            xr, xc, depth = q.popleft()
                            for nr, nc in (xr + 1, xc), (xr - 1, xc), (xr, xc + 1), (xr, xc - 1):
                                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == empty:
                                    grid[nr][nc] -= 1
                                    g[nr][nc] += depth + 1
                                    q.append((nr, nc, depth + 1))
                                    local_min = min(g[nr][nc], local_min)
                    empty -= 1
                    res = local_min
        return res if res != float('inf') else -1
""" 

1 -1 2 -1 1
-1 -1 -1 -1 -1
-1 -1 1 -1 -1

0 1 0 5 0
1 2 3 4 5
2 3 0 5 6

q = [(1, 0), (0, 1)]
local_min = inf
depth = 1






"""