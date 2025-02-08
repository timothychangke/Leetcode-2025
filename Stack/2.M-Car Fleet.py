class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort()
        res, time = 0, 0
        for pos, s in pairs[::-1]:
            t = (target - pos) / s
            if t > time:
                time = t
                res += 1
        return res
        