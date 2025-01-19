class MyHashMap:
    def __init__(self):
        self.map = {}
        
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        return self.map
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self.map[key]
        
    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]
        return self.map