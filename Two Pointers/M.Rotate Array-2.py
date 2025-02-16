class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rot(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k = k % len(nums)
        rot(0, len(nums) - 1)
        rot(0, k - 1)
        rot(k, len(nums) - 1)
        
""" 
1 2 3 4 5 6 7
7 6 5 4 3 2 1

"""