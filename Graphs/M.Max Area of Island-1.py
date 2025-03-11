class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] != 1:
                return 0
            grid[r][c] = -1
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(dfs(r, c), res)
        return res
