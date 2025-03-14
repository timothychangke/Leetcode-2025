class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r, c, v, prev):
            v.add((r, c))
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= prev and (nr, nc) not in v:
                    dfs(nr, nc, v, heights[nr][nc])
            return v
        po, ao = set(), set()
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    po |= dfs(i, j, set(), heights[i][j])
                if i == ROWS - 1 or j == COLS - 1:
                    ao |= dfs(i, j, set(), heights[i][j])
        return list(po & ao)