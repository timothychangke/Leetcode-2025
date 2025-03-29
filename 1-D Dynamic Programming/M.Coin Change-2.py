class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (len(amount) + 1)
        for i in range(1, len(amount)):
            dp[i] = min([dp[i - c] + 1 for c in coins if i - c >= 0] or [float('inf')])
        return dp[amount]
        
""" 
1. Initialise a dp array, where dp[i] is the fewest number of coins needed to make amount $i
2. Iterate through the dp, taking the minimum of the values of dp[i - c] where c are the values of the coins
3. Return dp[i]
"""