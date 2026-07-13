"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def __init__(self):
        self.map = {None: None}

    def getVal(self, node):
        if node in self.map:
            return self.map[node]

        self.map[node] = Node(x=-1)

        return self.map[node]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            copy = self.getVal(curr)
            copy.val = curr.val
            copy.next = self.getVal(curr.next)
            copy.random = self.getVal(curr.random)

            curr = curr.next
            
        return self.map[head]