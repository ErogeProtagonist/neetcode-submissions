# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        left_subtree = self.inorderTraversal(root.left)
        right_subtree = self.inorderTraversal(root.right)

        return left_subtree + [root.val] + right_subtree