class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, str):
            if left + right >= n * 2:
                res.append(str)
                return
            if left < n:
                dfs(left + 1, right, str + '(')
            if right < left and right < n:
                dfs(left, right + 1, str + ')')
        dfs(0, 0, '')
        return res