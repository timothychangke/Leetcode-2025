class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r, c):
            if r in range(rows) and c in range(cols):
                if (r, c) in cache: return cache[(r, c)]
                right = dfs(r, c + 1)
                bottom = dfs(r + 1, c)
                diagonal = dfs(r + 1, c + 1)
                cache[(r, c)] = 1 + min(right, bottom, diagonal) if matrix[r][c] == '1' else 0
        return max(cache.values())