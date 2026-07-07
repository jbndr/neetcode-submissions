# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0

            return (
                (node.val >= max_so_far)
                + dfs(node.left, max(max_so_far, node.val))
                + dfs(node.right, max(max_so_far, node.val))
            )

        return dfs(root, float("-inf"))

        


        

        




