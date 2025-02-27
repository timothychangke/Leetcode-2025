class ListNode():
    def __init__(self, val, prev, next):
        self.val, self.prev, self.next = val, prev, next
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.leftNode = ListNode(0, None, None)
        self.rightNode = ListNode(0, self.leftNode, None)
        self.leftNode.next = self.rightNode
        self.capacity = capacity
    
    def _insert(self, key, val):
        prev = self.rightNode.prev
        node = ListNode(val, prev, self.rightNode)
        prev.next = node
        self.rightNode.prev = node
        self.cache[key] = node

    def _remove(self, key):
        node = self.cache[key]
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        del self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self._remove(key)
            self._insert(key, val)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(key)
        if self.capacity > 0:
            self._remove(self.leftNode.next, key)
        self._insert(key, value)
        if len(self.cache) > self.capacity:
            self._remove(self.leftNode.next)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

