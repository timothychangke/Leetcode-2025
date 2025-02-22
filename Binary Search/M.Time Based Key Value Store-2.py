from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.d[key]) - 1
        while l < r:
            mid = l + (r - l) // 2
            res = 0
            if self.d[key][mid][1] > timestamp:
                r = mid
            else:
                res = mid
                l = mid + 1
        return res
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)