class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i in range(len(temperatures)):
            while s and temperatures[s[-1]] < temperatures[i]:
                idx = s.pop()
                res[idx] = i - idx
            s.append(i)
        return res


""" 
create a monotonically decreasing stack
if ele is larger, pop the stack and append the result array
[73,74,75,71,69,72,76,73]
res 1 1 0 0 0 0 0 0 
s 2 3 4 

 """