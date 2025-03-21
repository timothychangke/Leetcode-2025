class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        res = 0
        precol = [[0] * cols for r in range(rows)]
        for r in range(rows):
            lc = 0 
        
        for c in cols:
            lc, rc,  = 0, 0
            larr = [0] * rows
            rarr = [0] * rows
            for i in range(rows):
                larr[i] = lc
                lc = max(lc, heightMap[i][c])
            for i in range(rows - 1, -1, -1):
                rarr[i] = rc
                rc = max(rc, heightMap[i][c])
            for i in range(rows):
                water = max(0, min(rarr[i], larr[i]) - heightMap[i][c])
                res += water
        return res