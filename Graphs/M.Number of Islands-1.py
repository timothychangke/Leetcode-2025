class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == "1":
                    dfs(nr, nc)
            return 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": 
                    dfs(r, c)
                    res += 1
        return res
