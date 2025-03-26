class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        prev2, prev = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res = max(nums[i] + prev2, prev)
            prev, prev2 = res, prev
        return res
""" 
return the maximum value without choosing two consecutive values
the value at each step is either the sum of the values at the current step and 2 steps before or the step before
dp[i] = max(nums[i] + dp[i - 2], dp[i])
space can be optimised by using variables to represent these values

Learning points:
Since each i represents the most a robber can rob at that position, prev has to be set to the maximum of nums[0] and nums[1] 
"""