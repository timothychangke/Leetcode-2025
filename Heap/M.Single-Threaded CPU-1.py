import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        time = 0
        i = 0
        h = []
        tasks = sorted([(et, pt, idx) for idx, (et, pt) in enumerate(tasks)])
        while i < len(tasks) or h:
            while i < len(tasks) and tasks[i][0] <= time:
                enqueueTime, processingTime, idx = tasks[i]
                heapq.heappush(h, (processingTime, idx))  
                i += 1
            if h:
                processingTime, idx = heapq.heappop(h)
                time += processingTime
                res.append(idx)
            else:
                time = tasks[i][0]
        return res
