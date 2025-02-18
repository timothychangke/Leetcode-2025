from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.maxCount = 0
        self.countArr = defaultdict(list)
        self.counts = defaultdict(int)

    def push(self, val: int) -> None:
        self.counts[val] += 1
        self.maxCount = max(self.maxCount, self.counts[val])
        self.countArr[self.counts[val]].append(val)        

    def pop(self) -> int:
        res = self.countArr[self.maxCount].pop()
        self.counts[res] -= 1
        if not self.countArr[self.maxCount]:
            self.maxCount -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()