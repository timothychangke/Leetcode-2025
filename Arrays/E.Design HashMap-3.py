RANDOM_LARGE_PRIME_FOR_SIZE = 19997
RANDOM_LARGE_PRIME_FOR_MULT = 12582917


class ListNode:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.arr = [None for _ in range(RANDOM_LARGE_PRIME_FOR_SIZE)]

    def hash(self, val):
        return (val * RANDOM_LARGE_PRIME_FOR_MULT) % RANDOM_LARGE_PRIME_FOR_SIZE

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        h = self.hash(key)
        self.arr[h] = ListNode(key, value, self.arr[h])

    def get(self, key: int) -> int:
        h = self.hash(key)
        node = self.arr[h]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        node = self.arr[h]
        if not node:
            return
        if node.key == key:
            self.arr[h] = node.next
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return 
            node = node.next

        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)
