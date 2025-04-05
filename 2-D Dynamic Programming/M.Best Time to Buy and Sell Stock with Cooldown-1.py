class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rest, buy, sell = [0] * len(prices), [0] * len(prices), [0] * len(prices)
        rest[0], buy[0], sell[0] = 0, -prices[0], float('-inf')
        for i in range(1, len(prices)):
            rest[i] = max(rest[i - 1], sell[i - 1])
            buy[i] = max(rest[i - 1] - prices[i], buy[i - 1])
            sell[i] = buy[i - 1] + prices[i]
        return max(sell[-1], rest[-1])
        
""" 
There are essentially three states: rest, buy and sell
When you have bought, you can either sell or rest
When you have sold you must rest
When you have rested, you can either continue resting or sell more
Define three states of rested, buying and selling
for each state, the best outcome is based on what the best outcome of the previous states are
the result is the max between the last states of sell and rest (buy does not make sense here)
"""