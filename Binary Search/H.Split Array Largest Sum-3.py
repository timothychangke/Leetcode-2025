class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(mid):
            c = 1
            sum = 0
            for n in nums:
                sum += n
                if sum > mid:
                    sum = n
                    c += 1
                    if c > k:
                        return False
            return True
        l, r = max(nums), sum(nums)
        res = sum(nums)
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
