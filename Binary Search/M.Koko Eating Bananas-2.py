class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(c):
            return sum(math.ceil(n / c) for n in piles) <= h
        l, r = math.ceil(sum(piles) / h), max(piles)
        res = float('inf')        
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res