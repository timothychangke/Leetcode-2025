class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s
        res = [''] * numRows
        step = 1
        idx = 0
        for c in s:
            if idx == numRows - 1: step = -1
            elif idx == 0: step = 1
            res[idx] += c
            idx += step
        return ''.join(res)
        
""" 
Create an array of lines which represents the rows
go down the line for each letter until the bottom is reached, then go back up the line
append the rows together and return the string


res = [
'PA'
'AP'
'Y'
]
PAYPALISHIRING
"""