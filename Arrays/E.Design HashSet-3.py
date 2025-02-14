RANDOM_LARGE_PRIME_FOR_SIZE = 19997
RANDOM_LARGE_PRIME_FOR_MULT = 12582917

class ListNode:
    def __init__(self, key, next):
        self.key = key
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.s = [None for _ in range(RANDOM_LARGE_PRIME_FOR_SIZE)]

    def hash(self, value):
        return (value * RANDOM_LARGE_PRIME_FOR_MULT) % RANDOM_LARGE_PRIME_FOR_SIZE
    
    def add(self, key: int) -> None:
       if self.contains(key): return
       h = self.hash(key) 
       self.s[h] = ListNode(key, self.s[h])

    def remove(self, key: int) -> None:
        if not self.contains(key): return 
        h = self.hash(key)
        node = self.s[h]
        if not node: return False
        if node.key == key:
            self.s[h] = node.next
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return 
            node = node.next

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        node = self.s[h]
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