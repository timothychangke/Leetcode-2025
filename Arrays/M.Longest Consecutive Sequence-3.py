class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s, seen = set(nums), set()
        for n in nums:
            if n not in seen and n - 1 not in s:
                c = 0
                while n + c in s:
                    seen.add(n + c)
                    c += 1
                res = max(res, c)
        return res
