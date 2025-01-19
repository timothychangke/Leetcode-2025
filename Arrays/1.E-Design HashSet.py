class MyHashSet:

    def __init__(self):
        self.arr = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr.append(key)
        return self.arr
        
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.arr.remove(key)
        return self.arr

    def contains(self, key: int) -> bool:
        return key in self.arr