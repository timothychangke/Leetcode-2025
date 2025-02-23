class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(mid):
            c = 1
            sum = 0
            for w in weights:
                sum += w
                if sum > mid: 
                    sum = w
                    c += 1
                    if c > days:
                        return False
            return True
            
        l, r = max(weights), sum(weights)
        res = 0 
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res