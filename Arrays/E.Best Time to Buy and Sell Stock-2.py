class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res, l = 0, 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
        return res
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))