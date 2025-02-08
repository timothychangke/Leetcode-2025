from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.m = 0
        self.d = defaultdict(list)
        self.c = defaultdict(int)

    def push(self, val: int) -> None:
        self.c[val] += 1
        self.d[self.c[val]].append(val)
        self.m = max(self.m, self.c[val])

    def pop(self) -> int:
        res = self.d[self.m].pop()
        self.c[res] -= 1
        if not self.d[self.m]:
            self.m -= 1
        return res
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()