RANDOM_LARGE_PRIME_SIZE = 19997
RANDOM_LARGE_PRIME_MULT = 12582917

class ListNode:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.size = RANDOM_LARGE_PRIME_SIZE
        self.mult = RANDOM_LARGE_PRIME_MULT
        self.base = [None for _ in range(self.size)]
    
    def hash(self, key): 
        return (key * self.mult) % self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            h = self.hash(key)
            node = ListNode(key, self.base[h])
            self.base[h] = node

    def remove(self, key: int) -> None:
        h = self.hash(key)
        node = self.base[h]
        if not node: return 
        if node.key == key:
            self.base[h] = node.next
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        h = self.hash(key)    
        node = self.base[h]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)