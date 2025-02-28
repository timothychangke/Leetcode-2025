from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.freq = 1
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def length(self):
        return self.size
    
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev, node.next = prev, self.tail
        self.size += 1
        
    def remove(self, node=None):
        if self.size == 0:
            return 
        if not node:
            node = self.head.next
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        return node
        
class LFUCache:
    def __init__(self, capacity: int):
        self.f = defaultdict(DoublyLinkedList)
        self.d = {}
        self.minF = 0
        self.capacity = capacity
        self.size = 0
        
    def _update(self, node):
        freq = node.freq
        self.f[freq].remove(node)
        if self.minF == freq and self.f[freq].length() == 0:
            self.minF += 1
        node.freq += 1
        self.f[node.freq].insert(node)
        
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key in self.d:
            node = self.d[key]
            self._update(node)
            node.value = value
        else:
            if self.size == self.capacity:
                node = self.f[self.minF].remove()
                del self.d[node.key]
                self.size -= 1
            node = Node(key, value)
            self.d[key] = node
            self.f[1].insert(node)
            self.size += 1
            self.minF = 1  
