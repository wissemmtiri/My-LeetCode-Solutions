# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursive(node: TreeNode, path: str):
            if not node:
                return 0
            path += str(node.val)
            if not node.left and not node.right:
                return int(path)
            return recursive(node.left, path) + recursive(node.right, path)

        return recursive(root, '')