class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort()
        res, curTime = 0, 0
        for pos, sp in pairs[::-1]:
            time = (target - pos) / sp
            if time > curTime:
                curTime = time
                res += 1
        return res
