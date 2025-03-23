from collections import deque


class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10: return num
        i = 9
        res, pow = 0, 1
        while i >= 2:
            if num % i == 0:
                num //= i
                res += pow * i
                pow *= 10
            else:
                i -= 1
        return res if num == 1 and res < 2**31 - 1 else 0