class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        k = k % len(nums)
        rotate(0, len(nums) - 1)
        rotate(0, k - 1)
        rotate(k, len(nums) - 1)