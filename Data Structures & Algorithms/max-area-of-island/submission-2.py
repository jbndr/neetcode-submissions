class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        maxArea = 0

        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows:
                return 0

            if c < 0 or c >= columns:
                return 0

            if grid[r][c] == 0:
                return 0

            if (r,c) in visited:
                return 0

            visited.add((r,c))
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(rows):
            for c in range(columns):
                maxArea = max(dfs(r,c), maxArea)

        return maxArea



