class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_lookup = {val: i for i,val in enumerate(inorder)}
        self.idx = 0

        def build(left, right):
            if left > right:
                return None
                
            root = TreeNode(val=preorder[self.idx])
            self.idx += 1

            mid = index_lookup[root.val]

            root.left = build(left, mid-1)
            root.right = build(mid+1, right)

            return root

        return build(0, len(preorder)-1)