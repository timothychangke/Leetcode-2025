class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            n = abs(nums[i])
            if 0 < n <= len(nums):
                if nums[n - 1] > 0:
                    nums[n - 1] *=  -1
                elif nums[n - 1] == 0:
                    nums[n - 1] = (len(nums) + 1) * -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1