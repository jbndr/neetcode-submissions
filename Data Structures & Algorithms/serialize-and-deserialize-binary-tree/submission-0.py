# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""

        output = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                output.append("#")
            else:
                output.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(output)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None

        tokens = data.split(",")
        root = TreeNode(val=int(tokens[0]))
        queue = deque([root])

        i = 1
        while queue:
            node = queue.popleft()
            if tokens[i] != "#":
                node.left = TreeNode(val=int(tokens[i]))
                queue.append(node.left)
            i += 1
            if tokens[i] != "#":
                node.right = TreeNode(val=int(tokens[i]))
                queue.append(node.right)
            i += 1

        return root
