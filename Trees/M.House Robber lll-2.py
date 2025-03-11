# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            lwith, lwithout = dfs(node.left)
            rwith, rwithout = dfs(node.right)
            return (node.val + lwithout + rwithout, max(lwith, lwithout) + max(rwith, rwithout))
        left, right = dfs(root)
        return max(left, right)
