from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        row, col, square = defaultdict(set), defaultdict(set), defaultdict(set) 
        for r in range(ROWS):
            for c in range(COLS):
                ele = board[r][c]
                if ele == '.': continue
                if ele in row[r] or ele in col[c] or ele in square[(r // 3, c // 3)]:
                    return False
                row[r].add(ele)
                col[c].add(ele)
                square[(r // 3, c // 3)].add(ele)
        return True