import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y, x = -heapq.heappop(stones), -heapq.heappop(stones)
            if x == y:
                continue
            heapq.heappush(stones, x - y)
        return -stones[0] if stones else 0