# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, min_bound, max_bound):
            if not node:
                return True

            left = dfs(node.left, min_bound, node.val - 1)
            right = dfs(node.right, node.val + 1, max_bound)

            return min_bound <= node.val <= max_bound and left and right

        return dfs(root, float("-inf"), float("inf"))