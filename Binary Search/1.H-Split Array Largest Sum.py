class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def enough(mid):
            tot = 0
            res = 1
            for num in nums:
               tot += num
               if tot > mid:
                  res += 1
                  tot = num
                  if res > k:
                    return False
            return True
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) // 2
            if enough(mid):
                r = mid
            else:
                l = mid + 1
        return l