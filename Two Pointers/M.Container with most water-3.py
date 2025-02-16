class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                res = max(res, (r - l) * height[l])
                l += 1
            else:
                res = max(res, (r - l) * height[r])
                r -= 1
        return res
    
    """ 
    [1,8,6,2,5,4,8,3,7]
    l = 0
    r = 8
    res = 8
    """
