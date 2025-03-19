class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        prev = 1
        res = 2
        for i in range(2, n):
            temp = res
            res = temp + prev
            prev = temp
        return res