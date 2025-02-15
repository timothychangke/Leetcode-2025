from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        c = [[] for _ in range(len(nums) + 1)]
        count = 0
        res = []
        for key, val in n.items():
            c[val].append(key)
        for i in range(len(c) - 1, -1, -1):
            for n in c[i]:
                res.append(n)
                if len(res) >= k:
                    return res