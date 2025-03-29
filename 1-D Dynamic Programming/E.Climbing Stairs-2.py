class Solution:
    def climbStairs(self, n: int) -> int:
       if n < 2: return n
       prev, prev2, res = 1, 1, 0
       for _ in range(2, n + 1):
           res = prev + prev2
           prev2, prev = prev, res
       return res

""" 
 Ideation:
 Distinct ways to reach n when at each time you can climb 1 or 2 steps
 the distinct way to reach dp[i] = dp[i - 1] + dp[i - 2]
 
 for each value of i:
 dp[i] = dp[i - 1] + dp[i - 2]
 to save space, can use variables to represent the different values instead of an array

 """