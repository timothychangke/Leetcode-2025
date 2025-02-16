class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            while heights[i] < stack[-1]:
                h = stack.pop()
                res = max(res, (i - h) * heights[h])
            stack.append(i)
        return res