class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        m = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if m > diff:
                res = [[arr[i], arr[i + 1]]]
                m = diff
            elif m == diff:
                res.append([arr[i], arr[i + 1]])
        return res