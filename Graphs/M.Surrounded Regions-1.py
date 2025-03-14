class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        os = set((i, j) for i in range(ROWS) for j in range(COLS) if board[i][j] == 'O')
        print(os)
        def dfs(r, c, v):
            v.add((r, c))
            for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                if nr in range(ROWS) and nc in range(COLS) and board[nr][nc] == 'O' and (nr, nc) not in v:
                    dfs(nr, nc, v)
            return v
        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and board[i][j] == 'O':
                    os -= dfs(i, j, set())
        for i, j in os:
            board[i][j] = 'X'