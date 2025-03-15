import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ''
        c = Counter(s)
        if max(c.values()) > len(s) // 2: return ""
        h = [(-f, let) for let, f in c.items()]
        heapq.heapify(h)
        while h:
            f, let = heapq.heappop(h)
            if res and res[-1] == let:
                if not h: return ""
                f2, let2 = heapq.heappop()
                res += let2
                f2 += 1
                if f2 < 0: heapq.heappush((f2, let2))
            else:
                res += let
                f += 1
                if f < 0: heapq.heappush((f, let))
        return res
         