class Node:
    def __init__(self, key, val, prev, next):
        self.key, self.val, self.prev, self.next = key, val, prev, next
class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.leftNode = Node(0, 0, None, None)
        self.rightNode = Node(0, 0, self.leftNode, None)
        self.leftNode.next = self.rightNode
        self.capacity = capacity
        self.size = 0
        
    def insert(self, node):
        prevNode = self.rightNode.prev
        self.rightNode.prev = prevNode.next = node
        node.next, node.prev = self.rightNode, prevNode
    
    def remove(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        node = self.d[key]
        self.remove(node)
        self.insert(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
            self.size -= 1
        node = Node(key, value, None, None)
        self.d[key] = node
        self.insert(node)            
        self.size += 1
        if self.size > self.capacity: 
            print(self.leftNode.next.val)
            del self.d[self.leftNode.next.key]
            self.remove(self.leftNode.next)
            self.size -= 1

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)