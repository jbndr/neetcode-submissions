# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Given the preorder & inorder traversal of the same tree. Reconstruct the tree and return the root node.

        # Constraints:
        # - values are UNIQUE
        # - both traversals same size
        # - At least one node
        # - negative values allowed
        # - traversals do not contain null values

        # Examples:
        # [1] just return root Node with val preorder[0]

        # [1,2] preorder (root, left, right)
        # [2,1] inorder  (left, root, right)
        # what is the left vs right child?
        # root = 1
        # in in order we now, all to the left is part of the left
        # so this would be [1,2,null]

        # [1,2]
        # [1,2]
        # would be [1,null,2]

        # Ideas use preorder, to know where to split inorder
        # root = 1, find root in inorder, we then have left root right
        
        # Let's take the init example
        # preorder [1,2,3,5,4] # order of roots/parents
        # inorder [2,1,5,3,4]

        # root = [1]
        # split inorder [] [2] [] [1] [] [5] [] [3] [] [4] []
        # if single element, just child of current parent (in this case parent == root)
        # root.left = [2]
        
        if not preorder:
            return None

        root = TreeNode(val=preorder[0])

        index_of_root = inorder.index(root.val)
        left_inorder = inorder[:index_of_root]
        right_inorder = inorder[index_of_root+1:]

        root.left = self.buildTree(preorder[1:len(left_inorder)+1], left_inorder)
        root.right = self.buildTree(preorder[len(left_inorder)+1:], right_inorder)

        return root





