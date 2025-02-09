# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = peak = mid + 1
            else:
                r = mid
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) > target:
                r = mid - 1
            elif mountainArr.get(mid) < target:
                l = mid + 1
            else: return mid
        l, r = peak, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) > target:
                l = mid + 1
            elif mountainArr.get(mid) < target:
                r = mid - 1
            else: return mid
        return -1
    
    """ 
    while looking for the peak, can also look for the target
    """