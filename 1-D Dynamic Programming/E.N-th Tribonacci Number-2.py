class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1
        t1, t2, t3 = 0, 1, 1
        res = 0
        for _ in range(3, n + 1):
            res = t1 + t2 + t3
            t1, t2, t3 = t2, t3, res
        return res
    
    """ 
    Learning points:
    use variables instead of an array to save space
    """
        