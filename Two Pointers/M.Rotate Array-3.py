class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rot(start, end):
            l, r  = start, end - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
        rot(0, len(nums))
        rot(0, k)
        rot(k, len(nums))
        
""" 
1 2 3 4 5 6 7
7 6 5 4 3 2 1

"""