# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def dfs(node):
            nonlocal isValid

            if not node:
                return []

            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                if l >= node.val:
                    isValid = False

            for r in right:
                if r <= node.val:
                    isValid = False

            return [node.val] + left + right

        dfs(root)

        return isValid

        

        
        