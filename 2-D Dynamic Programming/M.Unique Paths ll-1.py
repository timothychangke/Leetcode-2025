class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[cols - 1] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c]: dp[c] = 0
                elif c + 1 < cols:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]
        

""" 
The most time and space efficient solution would involve dynamic programming with a space complexity of just two rows
Because the recurrence relation is just dp[r][c] = dp[r + 1][c] + dp[r][c + 1], only two rows are needed in this computation
"""