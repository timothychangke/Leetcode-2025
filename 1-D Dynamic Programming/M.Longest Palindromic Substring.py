class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0: return ''
        maxLen, res = 1, s[0]
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i]:
                    if i - j <= 2 or dp[j + 1][i - 1]:
                        dp[j][i] = True
                        if i - j + 1 > maxLen:
                            maxLen = i - j + 1
                            res = s[j:i + 1]
        return res
        
""" 
create a 2dp matrix, initially set everything to false
traverse the matrix via an i and j pointer
dp[j][i] represents whether the string s[j:i+1] is a palindrome
set dp[i][i] = True as they are the same letter
when i and j are equal, dp[j][i] is True if its length is <= 2 or dp[j + 1][i - 1] is True
save the max length palindrome

testcase
"badab"
    i
  j
res = aba
T F F F F
F T F T F
F F T F F
F F F T F
F F F F T
"""