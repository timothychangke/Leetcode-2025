class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2: return len(s)
        res = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
            for j in range(i):
                if s[i] == s[j]:
                    if i - j <= 2 or dp[j + 1][i - 1]:
                        dp[j][i] = True
                        res += 1
        return res
        
""" 
1. Initialise a 2d matrix with all False, dp[j][i] represents whether substring s[j: i + 1] is a palindrome
2. Initialise a res, and a maxlen
3. Traverse the matrix using two pointers: i(back), j(front)
 - set dp[i][i] to True as all single lettered strings are palindromes
 - if s[i] == s[j]
   - if i - j <= 2: set dp[j][i] to True (this handles cases like 'bb' or 'bab')
   - if dp[j + 1][i + 1] is True: set dp[j][i] to True (if the inner string is already a palindrome then s[j : i + 1] is a palindrome)
- Track the longest palindromic substring
- return res
"""