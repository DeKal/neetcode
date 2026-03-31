# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_max_height = self.maxHeight(root.left) if root.left else 0 
        right_max_height = self.maxHeight(root.right) if root.right else 0 
  
        if abs(left_max_height - right_max_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))