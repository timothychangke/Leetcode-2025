class Solution:
    def trap(self, height: List[int]) -> int:
        rightp, leftp = 0, 0
        leftprefix, rightprefix = [0 for _ in height], [0 for _ in height]
        res = 0
        for i in range(len(height)):
            leftprefix[i] = leftp
            leftp = max(height[i], leftp)
        for i in range(len(height) - 1, - 1, -1):
            rightprefix[i] = rightp
            rightp = max(height[i], rightp)
        print(rightprefix, leftprefix)
        for i in range(len(height)):
            water = min(leftprefix[i], rightprefix[i]) - height[i]
            res += water if water > 0 else 0
        return res
        