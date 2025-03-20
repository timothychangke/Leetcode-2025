import random
class RandomizedSet:

    def __init__(self):
        self.a, self.d = [], {}
        

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.a.append(val)
            self.d[val] = len(self.a) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            pos = self.d[val]
            val_of_last = self.a[-1]
            self.d[val_of_last] = pos
            self.a[pos] = val_of_last
            self.a.pop()
            del self.d[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return self.a[random.randint(0, len(self.a) - 1)]
    
    """ 
    ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
[[],[0],[1],[0],[2],[1],[]]
array = [1, 2]
dict = {1:0, 2:0}
    """


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()