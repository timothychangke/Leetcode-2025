class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, index):
            grid[r][c] = index
            res = 1
            for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                    res += dfs(nr, nc, index)
            return res
        index = 2
        area = {0: 0}
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1
        res = max(area.values())
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    connects = set(grid[nr][nc] for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] if nr in range(rows) and nc in range(cols))
                    res = max(res, 1 + sum(area[c] for c in connects))
        return res