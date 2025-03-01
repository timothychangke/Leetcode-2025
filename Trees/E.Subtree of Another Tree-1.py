# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        res = [False]
        def dfs(root):
            if not root: return 
            if isSame(root, subRoot): res[0] = True
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res[0]
        