class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = True
        res, b = 0, 0
        for i in range(len(prices) - 1):
            if stock and prices[i] > prices[i + 1]:
                stock = False
                res += prices[i] - prices[b]
            elif not stock and prices[i] < prices[i + 1]:
                stock = True
                b = i
        if stock:
            res += prices[len(prices) - 1] - prices[b]
        return res 