from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = len(nums) / 3
        res = []
        for key, val in c.items():
            if val > n:
                res.append(key)
                if len(res) >= 2:
                    break
        return res