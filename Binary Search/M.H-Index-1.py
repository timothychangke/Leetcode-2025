class Solution:
    def hIndex(self, citations: List[int]) -> int: 
        def feasible(n):
            count = 0
            for c in citations:
                if c >= n:
                    count += 1
            return count >= n
                
        l, r = 0, len(citations)
        res = 0
        while l <= r:
           mid = l + (r - l) // 2
           if feasible(mid):
               res = mid 
               l = mid + 1
           else:
               r = mid - 1
        return res