class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        maxArea = 0

        visited = set()

        def dfs(r, c, depth):
            if grid[r][c] == 0:
                return 0

            if (r,c) in visited:
                return 0

            visited.add((r,c))

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r_new = r + dx
                c_new = c + dy

                if r_new >= 0 and r_new < rows and c_new >= 0 and c_new < columns:
                    depth += dfs(r_new, c_new, 0)
            
            return depth + 1

        for r in range(rows):
            for c in range(columns):
                maxArea = max(dfs(r,c, 0), maxArea)

        return maxArea



