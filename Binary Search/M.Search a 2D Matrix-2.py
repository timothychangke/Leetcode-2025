class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ll, rr = 0, len(matrix) - 1
        row = -1 
        while ll <= rr:
            mid = ll + (rr - ll) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                row = mid
                break
            elif matrix[mid][-1] < target:
                ll = mid + 1
            else:
                rr = mid - 1
        if row == -1: return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target: 
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False