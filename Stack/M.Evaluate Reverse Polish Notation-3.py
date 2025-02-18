class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in '-+*/':
                s.append(int(t))
                continue
            e1 = s.pop()
            e2 = s.pop()
            if t == '+':
                res = e1 + e2
            elif t == '-':
                res = e2 - e1
            elif t == '*':
                res = e1 * e2
            elif t == '/':
                res = int(e2 / e1)
            s.append(res)
        return s[0]
                

