class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
                    
""" 
1. Initialise the dp array with the value of 1. index i represents the longest number of increasing subsequences starting from that number
2. Traverse the array in reverse, for each value, increment it by the max value it can reach for digits that are greater than it
3. Return dp[0]
"""