class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        prefix = 0
        for i in range(len(height)):
            leftMax[i] = prefix
            prefix = max(prefix, height[i])
        prefix = 0
        for i in range(len(height) - 1, - 1, -1):
            rightMax[i] = prefix
            prefix = max(prefix, height[i])
        for i in range(len(height)):
            water = min(leftMax[i], rightMax[i]) - height[i]
            res += water if water > 0 else 0
        return res
""" 
the minimum of the max height to the right of the block and the max height to the left of the block minus the current height of the block is how much water it can hold
"""