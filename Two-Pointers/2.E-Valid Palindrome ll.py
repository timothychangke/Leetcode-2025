class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s[:l] + s[l + 1:]) or self.isPalindrome(s[:r] + s[r + 1:])
            l += 1
            r -= 1
        return True
    def isPalindrome(self, s):
        return s == s[::-1]