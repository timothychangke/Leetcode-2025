from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        edgeOs = deque([(r, c) for r in range(ROWS) for c in [0, COLS - 1] if board[r][c] == 'O']) + deque([(r, c) for r in [0, ROWS - 1] for c in range(COLS) if board[r][c] == 'O'])
        while edgeOs:
            for _ in range(len(edgeOs)):
                r, c = edgeOs.popleft()
                board[r][c] = 'T'
                for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                    if r + dr in range(ROWS) and c + dc in range(COLS) and board[r + dr][c + dc] == 'O':
                        edgeOs.append((r + dr, c + dc))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T': board[r][c] = 'O'
                elif board[r][c] == 'O': board[r][c] = 'X'
                