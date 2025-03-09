import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones:
            s1 = -heapq.heappop(stones)
            if not stones:
                return s1
            s2 = -heapq.heappop(stones)
            if s1 == s2 and not stones:
                return 0
            else: heapq.heappush(stones, s2 - s1)