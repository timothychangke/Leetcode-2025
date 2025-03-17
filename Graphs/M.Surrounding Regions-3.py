class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            board[r][c] = 'T'
            for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                if nr in range(rows) and nc in range(cols) and board[nr][nc] == 'O':
                    dfs(nr, nc)
        for r in range(rows):
            for x in (0, cols - 1):
                if board[r][x] == 'O': dfs(r, x)
        for c in range(cols):
            for x in (0, rows - 1):
                if board[x][c] == 'O': dfs(x, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == 'T': board[r][c] = 'O'
            