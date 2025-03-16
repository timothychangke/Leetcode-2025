class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                    dfs(nr, nc)
            return 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res