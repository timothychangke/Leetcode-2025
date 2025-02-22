# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1
        peak = -1
        while l <= r:
            mid = l + (r - l) // 2
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                peak = mid
                r = mid - 1
            else:
                if mountainArr.get(mid) == target:
                    return mid
                l = mid + 1
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2
            midNum = mountainArr.get(mid)
            if midNum == target:
                return mid
            elif midNum > target:
                r = mid - 1
            else:
                l = mid + 1
        l, r = peak + 1, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            midNum = mountainArr.get(mid)
            if midNum == target:
                return mid
            elif midNum > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


            