class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.m = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for i in range(1, ROWS + 1):
            prefix = 0 
            for j in range(1, COLS + 1):
                prefix += matrix[i - 1][j - 1]
                self.m[i][j] = prefix + self.m[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.m[row2 + 1][col2 + 1] - self.m[row2 + 1][col1] - self.m[row1][col2 + 1] + self.m[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

""" 
0 0 0 0 
0 3 0 1
0 5 6 3
0 1 2 0

0 0 0 0 
0 3 3 4
0 8 17 
0 9 2 0
"""