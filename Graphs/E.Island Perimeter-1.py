class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                return 1
            if grid[r][c] == 1:
                grid[r][c] = -1
                return dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
            return 0
            

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res += dfs(i, j)
        return res