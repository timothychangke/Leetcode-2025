class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                    dfs(nr, nc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res