from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) / 2
        c = Counter(nums)
        for k, v in c.items():
            if v >= l:
                return k
