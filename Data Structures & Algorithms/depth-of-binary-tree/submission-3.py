# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        level = 0 

        while queue:
            size = len(queue)

            for _ in range(size):
                current = queue.popleft()

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            level += 1

        return level

        
        