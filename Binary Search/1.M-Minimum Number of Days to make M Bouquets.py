class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        def feasible(day):
            res = 0
            c = 0
            for bloom in bloomDay:
                if bloom <= day:
                    c += 1
                else:
                    res += c // k
                    c = 0
            res += c // k    
            return res >= m
        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l