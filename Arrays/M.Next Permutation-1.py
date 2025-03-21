class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                for j in range(len(nums) -1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        temp = nums[j]
                        nums[j] = nums[i - 1]
                        nums[i - 1] = temp
                        l, r = i, len(nums) - 1
                        while l < r:
                            temp = nums[l]
                            nums[l] = nums[r]
                            nums[r] = temp
                            l += 1
                            r -= 1
                        return 
        nums.reverse()
                            
                    
            
            