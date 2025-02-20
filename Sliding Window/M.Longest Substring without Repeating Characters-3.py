class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l += 1
            c.add(s[r])
            res = max(r - l + 1, res)
        return res
                  
