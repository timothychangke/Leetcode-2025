"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            isSame = True
            for dr in range(n):
                for dc in range(n):
                    if grid[r][c] != grid[r + dr][c + dc]:
                        isSame = False
            if isSame:
                return Node(grid[r][c], True, None, None, None, None)
            else:
                n = n // 2
                topLeft = dfs(n, r, c)
                topRight = dfs(n, r, c + n)
                bottomLeft = dfs(n, r + n, c)
                bottomRight = dfs(n, r + n, c + n)
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(len(grid), 0, 0)