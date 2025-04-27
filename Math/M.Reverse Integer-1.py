class Solution:
    def reverse(self, x: int) -> int:
        isNeg = (x < 0)
        x = abs(x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        if res > 2 ** 31 - 1: return 0
        return res * -1 if isNeg else res

        
""" 
Check for negative sign
Divide x by ten each time and take its remainder and add it to the res
x = 0
res = 321

x = 120
res = 21
 """