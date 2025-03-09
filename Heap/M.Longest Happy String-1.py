import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        heap = []
        for c, let, in [[a, 'a'], [b, 'b'], [c, 'c']]:
            if c > 0:
                heapq.heappush(heap, [-c, let])
        while heap:
            c, let = heapq.heappop(heap)
            if len(res) >=2 and res[-1] == res[-2] == let:
                if not heap: break
                c2, let2 = heapq.heappop(heap)
                res += let2
                c2 += 1
                if c2 < 0: heapq.heappush(heap, [c2, let2])
            else:
                res += let
                c += 1
                if c >= 0: continue
            heapq.heappush(heap, [c, let])
        return res
        
            
