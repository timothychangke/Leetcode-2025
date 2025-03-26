class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2: return min(cost[0], cost[1])
        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]

""" 
return the minimum cost of climbing stairs
this can be solved greedy as choosing the local minimum at each step will result in the global minimum

dp[i] = min(cost[i - 1], cost[i - 2])

 [10,15,20]
                i
        dp = [10, 15, 30, 0]
        
learning points:
Since the top of the stairs is one index greater than the len of cost, append a 0 such that the loop doesnt go out of range and that it is still mathematically correct
"""