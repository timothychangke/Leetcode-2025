class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[h])
            stack.append(i)
        return res