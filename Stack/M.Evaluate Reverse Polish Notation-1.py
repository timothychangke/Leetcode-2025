class Solution:
    def evalRPN(self, tokens: List[str]) -> int:    
        stack = []
        for token in tokens:
            if token not in '+-/*':
                stack.append(int(token))
            else:
                a, b = stack.pop(), stack.pop()
                if token == '*':
                    x = a * b
                elif token == '/':
                    x = int(b / a)
                elif token == '+':
                    x = a + b
                else:
                    x = b - a
                stack.append(x)
        return stack[0]