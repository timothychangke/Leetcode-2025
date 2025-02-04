class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res   
         
""" 
Initialise a monotonicly decreasing stack
when the temp is greater than the top of the stack, update the value at the top of the stack
keep popping until the temp is lower than the top of the stack, then push it into the stack
"""