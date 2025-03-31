class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if j ** 2 > i: break
                dp[i] = min(dp[i], dp[i - (j ** 2)] + 1)
        return dp[n]