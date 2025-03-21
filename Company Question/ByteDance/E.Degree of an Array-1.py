from collections import defaultdict 
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree, res, first, mapcount = 0, 0, {}, defaultdict(int)
        for i, a in enumerate(nums):
            if a not in first:
                first[a] = i
            mapcount[a] += 1
            if mapcount[a] > degree:
                res = i - first[a] + 1
                degree = mapcount[a]
            if mapcount[a] == degree:
                res = min(res, i - first[a] + 1)
        return res
            