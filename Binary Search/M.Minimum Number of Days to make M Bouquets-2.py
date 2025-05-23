class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        def feasible(x):
            ans = 0
            c = 0
            for b in bloomDay:
                if b <= x:
                    c += 1
                else:
                    ans += c // k
                    c = 0
            ans += c // k
            return ans >= m
        res = -1
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res