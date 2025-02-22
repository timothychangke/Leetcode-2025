class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def enough(x):
            c = 1
            s = 0
            for n in nums:
                s += n
                if s > x:
                    s = n
                    c += 1
                    if c > k:
                        return False
            return True
        l, r = max(nums), sum(nums)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if enough(mid):
                res = mid
                r = mid - 1 
            else:
                l = mid + 1
        return res