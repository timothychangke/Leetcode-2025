import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [((x * x + y * y), x, y) for x, y in points]
        heapq.heapify(points)
        return [(x, y) for _, x, y in heapq.nsmallest(k, points)]
        
        