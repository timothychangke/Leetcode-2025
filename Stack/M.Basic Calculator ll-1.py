class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, '+', []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+': stack.append(num)
                if sign == '-': stack.append(-num)
                if sign == '*': stack.append(int(stack.pop() * num))
                if sign == '/': stack.append(int(stack.pop() / num))
                num = 0
                sign = s[i]
        return sum(stack)
                    
            