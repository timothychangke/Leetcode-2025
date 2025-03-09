import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital, maxProfits = [], []
        minCapital = [[c, p] for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        for _ in range(k):
            while minCapital and minCapital[0][0] <= w:
                heapq.heappush(maxProfits, -heapq.heappop(minCapital)[1])
            if not maxProfits: break
            w += -heapq.heappop(maxProfits)
        return w
            
        