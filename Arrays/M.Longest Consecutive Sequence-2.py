class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        explored = set()
        res = 0
        for n in nums:
            if n in explored: continue
            if n - 1 not in s:
                c = 0
                while n + c in s:
                    explored.add(n + c)
                    c += 1
                res = max(res, c)
        return res