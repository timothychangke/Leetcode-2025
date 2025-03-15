import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        time = 0
        i = 0
        h = []
        while i < len(tasks):
            while tasks[i][0] < time:
                heapq.heappush(h, (tasks[i][1], i))
                i += 1
            processingTime, i = heapq.heappop(h)
            time += processingTime
            res.append(i)
        return res 