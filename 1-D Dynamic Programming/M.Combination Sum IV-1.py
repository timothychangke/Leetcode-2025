class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
        return dp[target]
        
        
""" 
1. Initialise a dp array of i where dp[i] represents the number of combinations that sum up to i
2. Iterate through the dp
 - check if i - n > 0, if so, increment the value of dp[i - n]
3. Return dp[target]

Test case:
[1,2,3], target = 4

"""