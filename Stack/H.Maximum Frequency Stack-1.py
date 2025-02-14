from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.map = {}
        self.arr = defaultdict(list)
        self.mf = 0

    def push(self, val: int) -> None:
        if val not in self.map:
            self.map[val] = 0
        self.map[val] += 1
        self.mf = max(self.mf, self.map[val])
        self.arr[self.map[val]].append(val)

    def pop(self) -> int:
        while not self.arr[self.mf]:
            self.mf -= 1
        self.map[self.arr[self.mf][-1]] -= 1
        return self.arr[self.mf].pop()
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()