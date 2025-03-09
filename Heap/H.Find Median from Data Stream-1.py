import heapq


class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
        if len(self.minHeap) < len(self.maxHeap): heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap): return float(self.minHeap[0])
        else: return (self.minHeap[0] - self.maxHeap[0]) / 2.0

        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()
