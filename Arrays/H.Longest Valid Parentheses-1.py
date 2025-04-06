class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, r * 2)
            elif r > l:
                l, r = 0, 0
        l, r = 0, 0
        for c in reversed(s):
            if c == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, r * 2)
            elif l > r:
                l, r = 0, 0
        return res
