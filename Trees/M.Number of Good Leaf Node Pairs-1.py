# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pairs = 0
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(node):
            if not node: return []
            if not node.left and not node.right: return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.pairs += 1
            both = left + right
            return [n + 1 for n in both]
        dfs(root)
        return self.pairs
