class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = intervals[0][0]
        r = 0
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
        
""" 
[[1,3],[2,6],[8,10],[15,18]]
l = 15
r = 10
res =[[1, 6], [8, 10]]

"""
            