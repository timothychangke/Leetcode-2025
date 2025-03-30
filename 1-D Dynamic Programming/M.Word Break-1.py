class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) + [True]
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:len(w) + i] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: break
        return dp[0]
                    
        
""" 
1. Initialise a dp array and solve it bottom up. set the very last index to be true
2. Each position i in the dp array represents whether the word can be broken up into the dictionary words
3. Iterate through each index and check first whether its length to the end of the array can fit the word. If it can, set the value of the index to be the value of the index + the length of the word it can fit
 - When it can match a word, break the loop
4. Return the value of dp[0]

Test Case:
s = "leetcode", wordDict = ["leet","code"]
leetcode
    i
i = 4
s[4:8]
dp = [F F F F F F F F T]
"""