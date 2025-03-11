# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return 
            dfs(node.left)
            dfs(node.right)
            if node.left.val == target: node.left = None
            if node.right.val == target: node.right = None
            return node
        return dfs(root, target)
        