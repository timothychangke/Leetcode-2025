import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        ctr = Counter(s)
        max_f = max(ctr.values())
        if max_f > (len(s) + 1) // 2:
            return ""
        heap = [[-c, let] for let, c in ctr.items()]
        heapq.heapify(heap)
        res = heapq.heappop(heap)[1]
        prev = res
        while heap:
            count, let = heapq.heappop(heap)
            if let == prev:
                count2, let2 = heapq.heappop(heap)
                res += let2
                count2 += 1
                if count2 < 0:
                    heapq.heappush([count2, let2])
            else:
                res += let
                count += 1
            if count < 0:
                heapq.heappush([count, let])
        return res
                