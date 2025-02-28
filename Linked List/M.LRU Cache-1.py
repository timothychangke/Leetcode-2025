class Node:
    def __init__(self, key, val, prev, next):
        self.key, self.val, self.prev, self.next = key, val, prev, next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, self.head, None)
        self.head.next = self.tail
    
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev
        del self.d[node.key]

    def _insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        self.d[node.key] = node

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
        node = Node(key, value, None, None)
        self._insert(node)
        if len(self.d) > self.capacity:
            self._remove(self.head.next)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)