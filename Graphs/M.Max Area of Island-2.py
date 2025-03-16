class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(r, c):
            res = 1
            grid[r][c] = 0
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    res += dfs(nr, nc)
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res