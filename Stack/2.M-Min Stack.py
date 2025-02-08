class MinStack:

    def __init__(self):
        self.s = []        

    def push(self, val: int) -> None:
        if self.s and val < self.s[-1][1]:
           self.s.append([val, val]) 
        elif self.s: self.s.append([val, self.s[-1][1]])
        else: self.s.append([val, val])
            
    def pop(self) -> None:
        return self.s.pop()[0]

    def top(self) -> int:
        return self.s[-1][0]        

    def getMin(self) -> int:
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()