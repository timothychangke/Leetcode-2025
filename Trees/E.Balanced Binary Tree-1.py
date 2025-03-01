# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1: res[0] = False
            return 1 + max(left, right)
        dfs(root)
        return res[0]
        