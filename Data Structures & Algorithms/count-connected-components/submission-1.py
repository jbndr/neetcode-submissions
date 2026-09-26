from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        connections = defaultdict(list)

        for a,b in edges:
            connections[a].append(b)
            connections[b].append(a)

        connected_components = 0

        def dfs(node, parent):
            if node in visited:
                return

            visited.add(node)

            outgoing = connections[node]

            for out in outgoing:
                if out != parent:
                    dfs(out, node)

        for i in range(n):
            if i in visited:
                continue
            
            dfs(i, None)

            connected_components += 1

        return connected_components


