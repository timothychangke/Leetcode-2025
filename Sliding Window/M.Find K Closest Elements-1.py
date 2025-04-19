class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def closer(a, b, x):
            if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b): return True
            else: return False            
        l = 0
        while l + k < len(arr):
            if closer(arr[l], arr[l + k], x):
                break
            else:
                l += 1
        return arr[l:l + k]
                
                