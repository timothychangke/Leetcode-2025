# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        self.res = []
        q = deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur: continue
                temp.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            self.res.append(temp)
        return self.res
