class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        area = 0
        for i in range(len(heights)):
            print(stack, heights[i])
            while heights[i] < heights[stack[-1]]:
                ele = stack.pop()
                area = max(area, heights[ele] * (i - ele))
            stack.append(i)
        return area




"""
find the previous smaller rectangle and the next smaller rectangle
the difference between these two points times the height of the current rectangle is the largest area including that rectangle
create a monotonically increasing stack
if height is greater than top, place it into the stack
the element that is below the current element in the stack is the previous smaller rectangle and the element that pops it off the stack is the next smaller rectangle
"""
        