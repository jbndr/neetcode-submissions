# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []

        def dfs(node, l):
            if not node:
                return

            dfs(node.left, l)

            l.append(node.val)

            dfs(node.right, l)

        dfs(root, sorted_list)

        return sorted_list[k-1]

            