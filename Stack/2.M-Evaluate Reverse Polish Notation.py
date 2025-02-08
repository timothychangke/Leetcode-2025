class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele not in '+*-/':
                stack.append(int(ele))
            else:
                a = stack.pop()
                b = stack.pop()
                if ele == '+':
                    stack.append(a + b)
                elif ele == '-':
                    stack.append(b - a)
                elif ele == '*':
                    stack.append(a * b)
                elif ele == '/':
                    stack.append(int(b / a))
        return stack[0]