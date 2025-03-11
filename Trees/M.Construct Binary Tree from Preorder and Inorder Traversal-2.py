# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        mid = inorder.index(preorder[0])
        return TreeNode(preorder[0], self.buildTree(preorder[1:mid + 1], inorder[:mid]), self.buildTree(preorder[mid + 1:], inorder[mid + 1:]))
        