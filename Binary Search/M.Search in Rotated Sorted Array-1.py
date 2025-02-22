class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            print(l, r)
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        
""" 

[4,5,6,7,0,1,2]

if mid > end of array
its in the left side
else in the rights side
check value against mid
if value is greater

"""