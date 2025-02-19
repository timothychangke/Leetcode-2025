class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            if r < l:
                l = r
                continue
            res = max(res, prices[r] - prices[l])
        return res