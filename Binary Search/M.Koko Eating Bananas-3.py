class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(mid):
            return sum(math.ceil(p / mid) for p in piles) <= h
        l, r = math.ceil(sum(piles) / h), max(piles)
        res = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res