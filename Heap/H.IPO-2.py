import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCap = [(c, p) for p, c in zip(profits, capital)]
        heapq.heapify(minCap)
        maxProfits = []
        for _ in range(k):
            while minCap and minCap[0][0] <= w:
                heapq.heappush(maxProfits, -heapq.heappop(minCap)[1])
            if not maxProfits: break
            w -= heapq.heappop(maxProfits)
        return w