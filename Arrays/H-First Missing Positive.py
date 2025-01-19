
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(l): 
            val = abs(nums[i])
            if 1 <= val <= l:
                if nums[val - 1] > 0:
                    nums[val - 1] = nums[val - 1] * -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = (l + 1) * -1
        for i in range(1, l + 1):
            if nums[i - 1] >= 0:
                return i
        return l + 1    
        
""" 
the array length is huge
nums can be positive or negative
O(n) time complexity and O(1) space complexity

have to modify the array in place so as to use constant space complexity
1. take out the negative numbers
2. using a similar idea to cyclic sort, map elements to the index of the array and use -negatives to denote that they are present
3. go through the array again and if the element in the index is not negative, that means it is not present
"""