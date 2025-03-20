class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2
        left = num[:mid]
        right = num[mid:]
        sl, sr = 0, 0
        ql, qr = 0, 0
        for n in left:
            if n == '?': ql += 1
            else: sl += int(n)
        for n in right:
            if n == '?': qr += 1
            else: sr += int(n)
        sum_diff = sl - sr
        q_diff = qr - ql
        return not (q_diff % 2 == 0 and (q_diff // 2) * 9 == sum_diff)