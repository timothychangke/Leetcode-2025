class Solution:
    def calculate(self, s: str) -> int:
        num, res, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                res += sign * num
                num = 0
                sign = [-1, 1][c == '+']
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign
    
""" 
(1+(4+5+2)-3)+(6+8)
            i 
 
num 3 
res 9
sign -1
stack = [  ]
"""
