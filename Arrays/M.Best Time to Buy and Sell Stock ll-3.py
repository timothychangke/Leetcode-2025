class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0) 
        res, have, buy = 0, False, 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1] and not have:
                have = True
                buy = i
            elif prices[i] > prices[i + 1] and have:
                have = False
                res += prices[i] - prices[buy]
        return res
    
""" 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(1, len(prices)):
            profit += prices[i] - prices[i-1] if (prices[i] - prices[i-1]) > 0 else 0
        
        return profit
            
"""
                 
            
            
        