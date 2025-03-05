class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)

        def dfs(x, y, index):
            res = 1
            grid[x][y] = index
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if i in range(ROWS) and j in range(COLS) and grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res

        index = 2
        area = {0: 0}
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1

        res = max(area.values())
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0:
                    islands = set(grid[x][y] for x, y in [
                                  (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if x in range(ROWS) and y in range(COLS))
                    res = max(res, sum(area[i] for i in islands) + 1)
        return res
