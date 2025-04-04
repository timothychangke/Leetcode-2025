class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = ceil(sum(stones) / 2)
        dp = {}
        def dfs(i, total):
            if total >= target or i == len(stones): return abs(total - (sum(stones) - total))
            if (i, total) in dp: return dp[(i, total)]
            else:
                dp[(i, total)] = min(dfs(i + 1, total + stones[i]), dfs(i + 1, total)) 
            return dp[(i, total)]           
        return dfs(0, 0)
       
""" 
The idea is to split the stones into two groups and have both of them be as equal to each other as possible. This would mean the differences in their sums would be as small as possible, and hence will be the smallest possible weight left
""" 