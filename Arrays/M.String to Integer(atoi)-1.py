class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i >= len(s): return 0
        res = 0
        sign = 1
        if s[i] == '+': i += 1
        elif s[i] == '-': 
            sign = -1
            i += 1
        while i < len(s):
            if not s[i].isdigit(): break
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        if res >= 2 ** 31 - 1: return 2 ** 31 - 1
        elif res < -(2 ** 31): return -(2 ** 31)
        return res
            
        
""" 
loop through each character of s
1. Skip left white space
2. Check for sign
3. Parse digits, if non-digit, break
4. Return digit according to bounds
 """