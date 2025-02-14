class MyQueue:

    def __init__(self):
        self.arr1 = []
        self.arr2 = []

    def push(self, x: int) -> None:
        self.arr1.append(x)        

    def pop(self) -> int:
        while not self.arr2 and self.arr1:
            self.arr2.append(self.arr1.pop())
        return self.arr2.pop()

    def peek(self) -> int:
        while not self.arr2 and self.arr1:
            self.arr2.append(self.arr1.pop())
        return self.arr2[-1]

    def empty(self) -> bool:
        return not self.arr1 and not self.arr2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()