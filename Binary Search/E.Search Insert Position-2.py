class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l 

""" 
[1, 2, 2, 2, 2, 3, 4, 5, 9, 16]
x = 2
l = 0 , r = 2
mid = 2
"""