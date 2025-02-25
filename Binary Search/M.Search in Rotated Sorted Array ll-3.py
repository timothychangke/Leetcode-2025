class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return True
            while r > mid and nums[r] == nums[mid]:
                r -= 1
            if nums[mid] <= nums[r]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
            