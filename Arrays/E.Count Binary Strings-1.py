class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = s[0]
        arr = []
        c = 0
        for n in s:
            if n != prev:
                arr.append(c)
                prev = n
                c = 0
            c += 1
        arr.append(c)
        res = 0
        for i in range(len(arr) - 1):
            res += min(arr[i], arr[i + 1])
        return res