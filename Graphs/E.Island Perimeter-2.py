class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(r, c):
            if  r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 1
            if grid[r][c] == 1:
                grid[r][c] = -1
                return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    res += dfs(r, c)
        return res
    
    
    """ 
    class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res += 4
                    if row > 0 and grid[row - 1][col] == 1:
                        res -= 2
                    if col > 0 and grid[row][col - 1] == 1:
                        res -= 2

        return res
    """
        