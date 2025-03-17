class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1: return -1
        arr = [0] * (n + 1)
        for a, b in trust:
            arr[a] -= 1
            arr[b] += 1
        for i in range(1, len(arr)):
            if arr[i] == n - 1: return i
        return -1