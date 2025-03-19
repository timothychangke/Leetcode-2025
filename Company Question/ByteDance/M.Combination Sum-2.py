class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(arr, i, sum):
            if sum == target:
                res.append(arr.copy())
                return 
            if i >= len(candidates) or sum > target: return 
            arr.append(candidates[i])
            dfs(arr, i, sum + candidates[i])
            arr.pop()
            dfs(arr, i + 1, sum)
        dfs([], 0, 0)
        return res