class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
        
        
        
""" 
return n where at each step, n is the sum of the last three previous numbers
dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

could hv used the same space optimisation as previously, which is to use variables to represent the 3 variables
"""