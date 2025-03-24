class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        res = float('inf')
        s = set(tuple(p) for p in points)
        for pi in points:
            for pj in points:
                    x1, y1 = pi
                    x2, y2 = pj
                    if x1 != x2 and y1 != y2:
                        if (x2, y1) in s and (x1, y2) in s:
                            res = min(res, abs(x2 - x1) * abs(y2 - y1))
        return res if res != float('inf') else 0