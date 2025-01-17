class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = False
        profit, buy_day = 0, 0
        for p in range(len(prices) - 1):
            if stock and prices[p + 1] < prices[p]:
                stock = False
                profit += (prices[p] - prices[buy_day])
            if not stock and prices[p + 1] > prices[p]:
                stock = True
                buy_day = p
        if stock:
            profit += (prices[-1] - prices[buy_day])
        return profit
        
        
""" 
every day there is three possible decisions
1. buy but only if you dont have the stock
2. do nothing
3. sell buy only if you have the stock

that means that each scenario will only have two decisions: buy/sell or do nothing

do dfs on a binary tree 

O(2^n)
"""