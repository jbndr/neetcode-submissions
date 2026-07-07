class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        rows = len(grid)
        columns = len(grid[0])

        visited = set()

        def dfs(node):
            visited.add(node)

            for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = node[0] + direction[0], node[1] + direction[1]
                if x >= 0 and x < rows and y >= 0 and y < columns:
                    if grid[x][y] == "1":
                        if (x,y) not in visited:
                            dfs((x,y))


        for r in range(rows):
            for c in range(columns):
                if (r, c) in visited:
                    continue
                
                if grid[r][c] == '0':
                    continue

                dfs((r,c))
                islands += 1

        return islands
        