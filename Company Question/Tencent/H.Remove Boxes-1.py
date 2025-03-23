class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(start, end, count=0):
            if start > end: return 0
            while start + 1 <= end and boxes[start] == boxes[start + 1]:
                start += 1
                count += 1
            sum = (count + 1)**2 + dp(start + 1, end)
            for x in range(start + 1, end + 1):
                if boxes[x] == boxes[start]:
                    sum = max(sum, dp(x, end, count + 1) + dp(start + 1, x - 1))
            return sum
        return dp(0, len(boxes) - 1)