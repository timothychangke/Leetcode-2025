class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, seq):
            if left < n:
                dfs(left + 1, right, seq + '(')
            if left > right:
                dfs(left, right + 1, seq + ')')
            if right == n:
                res.append(seq)
        dfs(0, 0, '')
        return res