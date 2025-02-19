class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]
    
""" 

x - arr[mid] > arr[mid + k] - x
is basically seeing if the left boundary is closer to x or the right boundary is closer to x


[0,0,1,2,3,3,4,7,7,8]
l = 0
r = 5
mid = 3
l = 0
k = 3
x = 1

"""