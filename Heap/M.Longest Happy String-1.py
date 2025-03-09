import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        prev = ''
        heap = [-a, 'a'], [-b, 'b'], [-c, 'c']
        heapq.heapify(heap)
        while heap:
            c, let = heapq.heappop(heap)
            if let == prev: return ""
            res.append(let + let if c > 1 else let)
            prev = let
            c += 1
            if c > 0:
                heapq.heappush([c, let])
        return res
            
