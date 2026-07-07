class Solution:
    def explore(self, board, start_row, start_col, target, visited) -> bool:
        if not target:
            return True

        if (start_row, start_col) in visited:
            return False

        if start_row < 0 or start_row >= len(board):
            return False

        if start_col < 0 or start_col >= len(board[0]):
            return False

        c = board[start_row][start_col]
        if not target.startswith(c):
            return False

        visited.add((start_row, start_col))

        dirs = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        for dx, dy in dirs:
            if self.explore(board, start_row+dx, start_col+dy, target[1:], visited):
                return True
        
        visited.remove((start_row, start_col))

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        for row in range(rows):
            for column in range(columns):
                if self.explore(board, row, column, word, set()):
                    return True

        return False


        
        


        