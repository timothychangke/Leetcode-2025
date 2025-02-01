from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        d = deque()
        for r in range(len(nums)):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            if l > d[0]:
                d.popleft()
            if r >= k - 1:
                l += 1
                res.append(nums[d[0]])
        return res