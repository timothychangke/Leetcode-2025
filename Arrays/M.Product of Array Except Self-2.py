class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        c = 1
        for i in range(len(nums)):
            res[i] = c
            c *= nums[i]
        c = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= c
            c *= 1
        return res


""" 
c = 24
[1, 2, 3, 4]
 1, 1, 2, 6
    12   8   6 
"""
