from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r  = 0, len(nums) - 1
        res = deque()
        while l <= r:
            sl, sr = nums[l] ** 2, nums[r] ** 2
            if sl > sr:
                res.appendleft(sl)
                l += 1
            else:
                res.appendleft(sr)
                r -= 1
        return list(res)
