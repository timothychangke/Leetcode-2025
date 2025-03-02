class Node:
    def __init__(self, val, prev, next):
        self.val, self.prev, self.next = val, prev, next

class MyCircularQueue:

    def __init__(self, k: int):
        self.leftNode = Node(0, None, None)
        self.rightNode = Node(0, self.leftNode, None)
        self.leftNode.next = self.rightNode
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        prev = self.rightNode.prev
        node = Node(value, prev, self.rightNode)
        prev.next = node
        self.rightNode.prev = node
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        nextNode = self.leftNode.next.next
        self.leftNode.next = nextNode
        nextNode.prev = self.leftNode
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.leftNode.next.val
        return self.rightNode.prev.val
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rightNode.prev.val
        

    def isEmpty(self) -> bool:
        return self.leftNode.next == self.rightNode
        

    def isFull(self) -> bool:
        return self.size >= self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()