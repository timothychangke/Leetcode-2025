from collections import defaultdict


class ListNode():
    def __init__(self, key, value, prev=None, next=None):
        self.key, self.value, self.prev, self.next = key, value, prev, next
        self.freq = 1


class DoublyLinkedList():
    def __init__(self):
        self.leftNode = ListNode(0, 0)
        self.rightNode = ListNode(0, 0, self.leftNode, None)
        self.leftNode.next = self.rightNode
        self.size = 0

    def length(self):
        return self.size
    
    def insert(self, node):
        prevNode = self.rightNode.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.rightNode
        self.rightNode.prev = node
        self.size += 1

    def remove(self, node=None):
        if self.size == 0:
            return None
        if not node:
            node = self.leftNode.next
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.freq = defaultdict(DoublyLinkedList)
        self.d = {}
        self.minF = 0
        self.capacity = capacity
        self.size = 0
        
    def _update(self, node):
        f = node.freq
        self.freq[f].remove(node)
        if self.minF == f and self.freq[f].length() == 0:
            del self.freq[f]  
            self.minF += 1
        node.freq += 1
        self.freq[node.freq].insert(node)
        self.d[node.key] = node  

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
            node.value = value  
            self._update(node)
        else:
            if self.size >= self.capacity:
                node = self.freq[self.minF].remove()
                del self.d[node.key]
                self.size -= 1
            node = ListNode(key, value)
            self.minF = 1
            self.freq[self.minF].insert(node)
            self.d[key] = node
            self.size += 1
