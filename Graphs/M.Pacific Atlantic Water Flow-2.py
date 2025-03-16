class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        def dfs(r, c, ocean):
            ocean[r][c] = True
            for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                if nr in range(rows) and nc in range(cols) and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        res = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]: res.append([r, c])
        return res