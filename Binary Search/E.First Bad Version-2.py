# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
    
    
""" 
n = 5, bad = 4

0 1 2 3 4 5
if while is l < r

0 1 2 3 4 5
if while is l <= r



"""
