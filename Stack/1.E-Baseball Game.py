class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for op in operations:
            if s and op == 'C':
                s.pop()
            elif s and op == 'D':
                s.append(s[-1] * 2)
            elif len(s) >= 2 and op == '+':
                s.append(s[-1] + s[-2])
            else:
                s.append(int(op))
        return sum(x for x in s)
            