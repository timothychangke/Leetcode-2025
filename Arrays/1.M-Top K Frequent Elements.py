from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        count = 0
        freq = [[] for i in range((len(nums) + 1))]
        res = []
        for key, value in c.items():
            freq[value].append(key)
        print(c)
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res