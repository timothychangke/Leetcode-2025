class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = s[0], 1
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res
