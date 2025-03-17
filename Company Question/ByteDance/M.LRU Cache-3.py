class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.frontNode = ListNode(0, 0)
        self.backNode = ListNode(0, 0)
        self.frontNode.next = self.backNode
        self.backNode.prev = self.frontNode
    
    def insert(self, node):
        prev = self.backNode.prev
        prev.next = node
        self.backNode.prev = node
        node.next, node.prev = self.backNode, prev

    def remove(self, node=None):
        if not node: node = self.frontNode.next
        nextNode, prevNode = node.next, node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode
        return node
        
    def get(self, key: int) -> int:
        if key not in self.dict: return -1
        node = self.dict[key]
        self.remove(node)
        self.insert(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.size >= self.capacity:
                nodeRemoved = self.remove()
                del self.dict[nodeRemoved.key]
                self.size -= 1
            node = ListNode(key, value)
            self.dict[key] = node
            self.insert(node)
            self.size += 1
        else:
            node = self.dict[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)