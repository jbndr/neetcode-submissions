# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return

            left = node.left
            right = node.right

            dfs(left)
            dfs(right)
            
            if left and left.val == target:
                if not left.left and not left.right:
                    node.left = None
            if right and right.val == target:
                if not right.left and not right.right:
                    node.right = None

        dfs(root)

        if root and root.val == target:
            if root.left == root.right == None:
                return None

        return root
        