class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        i = 1
        while i + 1 < len(arr):
            if arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                l = i - 1
                r = i + 1
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1
                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1
                res = max(res, r - l + 1)
                i = r
            else: i += 1
        return res