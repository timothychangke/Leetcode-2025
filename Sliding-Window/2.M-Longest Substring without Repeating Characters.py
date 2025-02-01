class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        res = 0
        for end in s:
            while end in window:
                window.remove(s[start])
                start += 1
            window.add(end)
            res = max(res, len(window))
        return res
