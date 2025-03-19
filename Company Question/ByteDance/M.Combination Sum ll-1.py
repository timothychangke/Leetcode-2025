class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(arr, i, sum):
            print(arr)
            if sum == target: 
                res.append(arr.copy()) 
                return 
            if i >= len(candidates) or sum > target: return 
            arr.append(candidates[i])
            dfs(arr, i + 1, sum + candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(arr, i + 1, sum)
        dfs([], 0, 0)
        return res
    
a = Solution()
a.combinationSum2([2, 5, 2, 1, 2], 5)
    
""" 
res = [1, 2, 2]
[2, 5, 2, 1, 2]
[1, 2, 2, 2, 5]
arr = [1]
dfs()
arr = [1, 2]
dfs()
arr = [1, 2, 2]
return 
arr = [1, 2]


"""