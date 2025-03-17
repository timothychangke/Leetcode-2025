class Solution:
    def trap(self, height: List[int]) -> int:
        lb, rb = 0, 0
        leftBound = [0] * len(height)
        rightBound = [0] * len(height)
        for h in range(len(height)):
            leftBound[h] = lb
            lb = max(lb, height[h])
        for h in range(len(height)-1, -1, -1):
            rightBound[h] = rb
            rb = max(rb, height[h])
        res = 0
        for h in range(len(height)):
            water = min(leftBound[h], rightBound[h]) - height[h]
            res += water if water > 0 else 0
        return res