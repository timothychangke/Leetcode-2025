class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = l = 0
        for r in range(len(s)):
            while l < r and s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, len(window))
        return res