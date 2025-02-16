class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for op in operations:
            if res and op == 'C':
                res.pop()
            elif res and op == 'D':
                res.append(res[-1] * 2)
            elif len(res) >= 2 and op == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        return sum(res)
