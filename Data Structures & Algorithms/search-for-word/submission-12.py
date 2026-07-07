class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            # trying to match word[i] at (r, c)
            if i == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if board[r][c] == "#":
                return False
            if board[r][c] != word[i]:
                return False

            tmp = board[r][c]

            board[r][c] = "#"                           # choose
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if backtrack(r + dr, c + dc, i + 1):        # explore
                    return True
            board[r][c] = tmp                         # un-choose
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False