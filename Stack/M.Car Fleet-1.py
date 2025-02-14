class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = endtime = 0
        pairs = [[position[i], speed[i]] for i in range(len(speed))]
        for pos, s in sorted(pairs)[::-1]:
            duration = (target - pos) / s 
            if duration > endtime:
                endtime = duration
                res += 1
        return res 
            
            