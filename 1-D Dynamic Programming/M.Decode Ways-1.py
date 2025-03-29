class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0': 
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')): dp[i] += dp[i + 2]
        return dp[0]
        
""" 
1. Create a dp array and traverse it backwards
2. Let dp[i] = dp[i + 1]
3. If dp[i] != 0: increment it by one, else set dp[i] = 0 as the number '06' for example is invalid
4. Now consider the 2 digit scenario, if any of these scenarios are true, increment by dp[i + 2] as the number of times it can be interpreted is the number of times you interpret it as one number + number of times you interpret it as two numbers:
 - If i = 1, then i + 1 can be from 0 - 9
 - If i = 2, then i can be from 0 - 6
return dp[0][0]

Test case:
226
dp = [3 2 1]

Learnings: 
Take not of the and and or conditions as well as dp[i] += dp[i + 2] reasonings
"""