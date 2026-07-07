# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, []

            left_valid, left = dfs(node.left)
            right_valid, right = dfs(node.right)

            is_valid = left_valid and right_valid

            for l in left:
                if l >= node.val:
                    is_valid = False

            for r in right:
                if r <= node.val:
                    is_valid = False

            return is_valid, [node.val] + left + right

        is_valid, _ = dfs(root)
        return is_valid