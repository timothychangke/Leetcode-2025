class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        v = set()
        for r in range(len(s)):
            while s[r] in v:
                v.remove(s[l])
                l += 1
            v.add(s[r])
            res = max(r - l + 1, res)
        return res
            