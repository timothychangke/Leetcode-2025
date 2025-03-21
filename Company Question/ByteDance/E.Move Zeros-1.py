class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if not nums[i]: continue
            temp = nums[i]
            nums[i] = 0
            nums[k] = temp
            k += 1