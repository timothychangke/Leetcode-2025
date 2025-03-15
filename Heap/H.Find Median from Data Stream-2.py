import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
        if len(self.maxHeap) > len(self.minHeap): heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2: return self.minHeap[0]
        else: return (-self.maxHeap[0] + self.minHeap[0]) / 2
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()