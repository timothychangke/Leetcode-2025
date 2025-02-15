class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = res = 0
        for r in range(len(prices)):
            if prices[r] <= prices[l]: 
                l = r
                continue
            res = max(prices[r] - prices[l], res)
        return res
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))