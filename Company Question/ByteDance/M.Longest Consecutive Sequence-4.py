class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num, v = set(nums), set()
        for n in nums:
            if n in v: continue
            if n - 1 not in num:
                temp = 0
                while n + temp in num:
                    v.add(n + temp)
                    temp += 1
                res = max(res, temp)
        return res        