class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            temp = curMax
            curMax = max(n * curMin, n * curMax, n)
            curMin = min(n * curMin, n * temp, n)
            res = max(res, curMax)
        return res
        
""" 
1. Create a dp array with the length of nums
2. For each element, save the minimum product and maximum product. The minimum product is needed in the case that the next value is negative whereby a negative * minimum product could give a maximum value
3. There is also a case where the number 0 might affect the max and min. If a zero is met, simply take the next number
4. Space optimisation would be to save the variables as mins and maxs, without the need of an dp array

Learnings:
- Save both the current mins and max in the event that a negative number is next in line
- To account for zeros, include the value n into the min and max
- set res initially to zero to account for the event when nums contains only 0s or negative elements
"""