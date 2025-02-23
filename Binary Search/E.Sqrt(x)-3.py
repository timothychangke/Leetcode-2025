class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res