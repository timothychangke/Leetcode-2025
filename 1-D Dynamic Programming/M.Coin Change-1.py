class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
        return [dp[amount], -1][dp[amount] == float('inf')]
    
""" 
1. Initialise a dp array with lenght of amount plus 1 (take into account that it is zero indexed). Make sure the 0th value is 0 such that the result of the dp[i] = dp[i - c] + 1 is valid
2. Iterate through the dp array
3. Find the minimum value when i is subtracted with the coin value, but only if i - c is a valid index
4. Return the value of amount in the dp array but only if it is valid

Test Case:
[1,2,5], amount = 11
     c
dp = [0 1 1 2 2 1 m m m m m m ]
                  i
Learnings:
Starting index has to be zero to allow for valid incrementing of coin amount
list comprehension is always done in the list
must have a else case for list comprehension or not the array will error if its a min(undefined)

"""
