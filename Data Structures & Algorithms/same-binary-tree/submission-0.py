# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def tree_rep(root):
            rep = []
            def dfs(root):
                nonlocal rep

                if not root:
                    rep.append(None)
                    return

                rep.append(root.val)

                dfs(root.left)
                dfs(root.right)

            dfs(root)

            return rep

        return tree_rep(q) == tree_rep(p)

        