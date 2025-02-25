class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        def feasible(mid):
            c = 0
            sum = 0
            for b in bloomDay:
                if b <= mid:
                    sum += 1
                else:
                    c += sum // k
                    sum = 0
            c += sum // k
            return c >= m
        l, r = min(bloomDay), max(bloomDay)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res