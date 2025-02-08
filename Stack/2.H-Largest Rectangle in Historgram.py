class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                res = max(res, (i - idx) * heights[idx])
            stack.append(i)
        return res

            