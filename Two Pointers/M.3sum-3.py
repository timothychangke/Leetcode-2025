class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l + 1]:
                            l += 1
        return res
        
        
""" 
for n = 2 to n = len(nums) - 1
if repeat: skip
    perform two sum on the range of numbers after it 
    if repeat, skip
    
[-1,0,1,2,-1,-4]
[-4, -1, -1, 0, 1, 2]
i = 1
l = 1
r = 5
1
"""