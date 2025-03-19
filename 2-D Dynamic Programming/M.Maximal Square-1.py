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