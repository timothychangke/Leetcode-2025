class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            ans = 1
            c = 0
            for w in weights:
                c += w
                if c > capacity:
                    c = w
                    ans += 1
                    if ans > days:
                        return False
            return True 
        l, r = max(weights), sum(weights)
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        