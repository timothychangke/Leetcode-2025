class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t = []
        for cap, start, end in trips:
            t.append([start, cap])
            t.append([end, -cap])
        cur = 0
        for pos, cap in sorted(t):
            cur += cap
            if cur > capacity: return False
        return True