class ListNode:
    def __init__(self, val, left, right):
        self.val, self.left, self.right = val, left, right

class LRUCache:

    def __init__(self, capacity: int):
        self.leftNode = (0, None, None)
        self.rightNode = (0, self.leftNode, None)
        self.leftNode.right = self.rightNode
        self.cache = {}
        self.capacity = capacityk

    def get(self, key: int) -> int:
        
        

    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)