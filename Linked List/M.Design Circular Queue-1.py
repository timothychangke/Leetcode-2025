class ListNode:
    def __init__(self, val, left, right):
        self.val, self.left, self.right = val, left, right


class MyCircularQueue:

    def __init__(self, k: int):
        self.leftNode = ListNode(0, None, None)
        self.rightNode = ListNode(0, self.leftNode, None)
        self.leftNode.right = self.rightNode
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        node = ListNode(value, self.rightNode.left, self.rightNode)
        self.rightNode.left.right = node
        self.rightNode.left = node
        self.k -= 1
        return True
            
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        next = self.leftNode.right.right
        self.leftNode.right = next
        next.left = self.leftNode
        self.k += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.leftNode.right.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rightNode.left.val

    def isEmpty(self) -> bool:
        return self.leftNode.right == self.rightNode

    def isFull(self) -> bool:
        return self.k <= 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
