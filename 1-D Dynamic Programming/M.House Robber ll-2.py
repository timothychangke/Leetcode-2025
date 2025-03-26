class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def robbery(n):
            if len(n) == 1: return n[0]
            if len(n) == 2: return max(n[0], n[1])
            prev2, prev = n[0], max(n[0], n[1])
            res = 0
            for i in range(2, len(n)):
                res = max(prev2 + n[i], prev)
                prev2, prev = prev, res
            return res
        return max(robbery(nums[:-1]), robbery(nums[1:]))
    
""" 
Idea:
Same as house robber one, just that you have to perform the robbing on the the array without the last index and once more without the first index and find the max. This is because it is a cycle, either you include the starting point or you dont

Learning Points:
have to account if the initial input array is of length 1
robbery is also until the len of the nums array
"""