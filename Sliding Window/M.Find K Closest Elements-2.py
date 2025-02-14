class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def closest(a, b, x):
            if abs(arr[a] - x) < abs(arr[b] - x) or (abs(arr[a] - x) == abs(arr[b] - x) and arr[a] < arr[b]): return True
            else: return False
        r = k
        while r < len(arr):
            if closest(r - k, r, x):
                break
            else: r += 1
        return arr[r-k:r]