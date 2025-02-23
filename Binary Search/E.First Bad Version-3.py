# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        res = n + 1
        while l <= r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res