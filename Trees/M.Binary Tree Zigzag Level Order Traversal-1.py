# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root: return []
            res = []
            q = deque([root])
            l = 0 
            while q:
                l += 1
                level = []
                for _ in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if l % 2 == 0:
                    level.reverse()
                res.append(level)
            return res
        return bfs(root)