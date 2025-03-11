# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = deque([root])
        while q:
            right = None
            for _ in range(len(q)):
                cur = q.popleft()
                right = cur.val
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(right)
        return res