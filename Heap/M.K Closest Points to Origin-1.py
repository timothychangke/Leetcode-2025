import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[x*x + y*y, x, y] for x, y in points]
        heapq.heapify(dist)
        return [[x, y] for dist, x, y in heapq.nsmallest(k, dist)]
        