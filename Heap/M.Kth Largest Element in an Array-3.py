import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       n = [-i for i in nums]
       heapq.heapify(n)
       for _ in range(k - 1):
           heapq.heappop(n)
       return -heapq.heappop(n)