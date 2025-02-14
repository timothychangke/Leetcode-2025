class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, str):
            if len(str) == n * 2:
                res.append(str)
            if left < n:
                dfs(left + 1, right, str + '(')
            if right < left:
                dfs(left, right + 1, str + ')')
        dfs(0, 0, '')
        return res
                