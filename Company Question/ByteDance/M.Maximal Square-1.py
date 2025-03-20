class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols): return 0
            if (r, c) not in cache: 
                right = dfs(r, c + 1)
                bottom = dfs(r + 1, c)
                diagonal = dfs(r + 1, c + 1)
                cache[(r, c)] = 1 + min(right, bottom, diagonal) if matrix[r][c] == '1' else 0
            return cache[(r, c)]
        dfs(0, 0)
        s = max(cache.values())
        return s * s
    
    """ 
    class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
    """