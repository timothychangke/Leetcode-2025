class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, r, b = 0, 0, len(nums) - 1
        while i <= b:
            print(nums)
            if nums[i] == 0:
                nums[i], nums[r] = nums[r], 0
                r += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], 2
                b -= 1
                i -= 1
            i += 1
                
                
""" 
0 0 1 1 2 2
r: 2
b: 3
i: 2

"""          
        