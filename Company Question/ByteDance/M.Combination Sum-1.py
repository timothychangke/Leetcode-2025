class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, arr, c):
            if c == target:
                res.append([*arr])
                return 
            if c > target or i >= len(candidates): return
            arr.append(candidates[i])
            dfs(i, arr, c + candidates[i])
            arr.pop()
            dfs(i + 1, arr, c)
        dfs(0, [], 0)
        return res