"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = defaultdict(list)
        visited = set()

        if not node:
            return None

        queue = [node]

        while queue:
            curr = queue.pop()
            val = curr.val
            if val not in visited:
                visited.add(val)
                for n in curr.neighbors:
                    graph[val].append(n.val)
                    queue.append(n)

        nodes = {}

        def build_node(val, neighbors):
            if val in nodes:
                return nodes[val]
            
            nodes[val] = Node(val=val)
            nodes[val].neighbors = [build_node(v, graph[v]) for v in neighbors]

            return nodes[val]

        return build_node(1, graph[1])
