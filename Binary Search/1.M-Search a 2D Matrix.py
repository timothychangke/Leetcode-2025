class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ll, rr = 0, len(matrix) - 1
        while ll <= rr:
            mid = ll + (rr - ll) // 2
            if target > matrix[mid][-1]:
                ll = mid + 1
            elif target < matrix[mid][0]:
                rr = mid - 1
            else:
                break
        else:
            return False
        l, r = 0, len(matrix[0]) - 1
        row = ll + (rr - ll) // 2
        while l <= r:
            middle = l + (r - l) // 2
            if matrix[row][middle] < target:
                l =  middle + 1
            elif matrix[row][middle] > target:
                r = middle - 1
            else:
                return True
        return False
        
        