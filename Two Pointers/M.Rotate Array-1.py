class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseArr(start, end):
            while start < end:
                tmp = nums[end]
                nums[end] = nums[start]
                nums[start] = tmp
                start += 1
                end -= 1
        k = k % len(nums)
        reverseArr(0, len(nums) - 1)
        reverseArr(0, k - 1)
        reverseArr(k, len(nums) - 1)

        