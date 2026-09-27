class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        directions = [
            (-1,0),
            (0,1),
            (1,0),
            (0,-1)
        ]

        def dfs(r,c, visited):
            visited.add((r,c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visited and heights[nr][nc] <= heights[r][c]:
                    dfs(nr, nc, visited)
                elif nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                    visited.add((nr,nc))

        output = []

        ROWS = len(heights)
        COLS = len(heights[0])

        for r in range(ROWS):
            for c in range(COLS):

                visited = set()

                dfs(r,c, visited)

                pacific_reached = [True for (r,c) in visited if r < 0 or c < 0]
                atlantic_reached = [True for (r,c) in visited if r == ROWS or c == COLS]

                if True in pacific_reached and True in atlantic_reached:
                    output.append((r,c))

        return output

                


        