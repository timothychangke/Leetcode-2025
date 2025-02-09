class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def calDays(cap):
            res = 1
            total = 0
            for i in weights:
                total += i 
                if total > cap:
                    total = i
                    res += 1
                    if res > days:
                        return False
            return True 
        minCap, maxCap = max(weights), sum(weights)
        while minCap < maxCap:
            mid = (minCap + maxCap) // 2
            if calDays(mid):
                maxCap = mid
            else:
                minCap = mid + 1
        return maxCap


""" 
minimally the ship must have capacity to take the heaviest weight 
the optimal solution is to sum up all the weights and divide by the number of days
for the minimal requirement is the max of these two values

the max is then the sum of all the weights

then now i do a binary search on the capacities and tally it with the days
"""

sol = Solution()
print(sol.shipWithinDays([3, 2, 2, 4, 1, 4], 5))
