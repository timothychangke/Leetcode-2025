from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict, col_dict, square_dict = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == '.': continue
                if ele in row_dict[r] or ele in col_dict[c] or ele in square_dict[(r // 3, c // 3)]:
                    return False
                row_dict[r].add(ele)
                col_dict[c].add(ele)
                square_dict[(r//3, c//3)].add(ele)
        return True

""" 
board 9 rows 9 colums
each square will only be 1-9 or .

create a set for each row, for each col and for each sub square
sub sqaure key will be r // 3, c // 3
for each square ill add to set
if already in set return false
if finish loop return True

O(rc)
"""