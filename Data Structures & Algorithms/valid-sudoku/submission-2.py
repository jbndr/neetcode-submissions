class Solution:
    def sub_box_is_valid(self, board, start_row, start_col):
        nums = set()

        for i in range(3):
            for j in range(3):
                cell = board[start_row + i][start_col + j]
                if cell != "." and cell in nums:
                    return False
                else:
                    nums.add(cell)
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows
        for i in range(9):
            nums = set()
            for j in range(9):
                cell = board[i][j]
                if cell != "." and cell in nums:
                    print(f"Failing row check at {i}{j}")
                    return False
                else:
                    nums.add(cell)

        # Check columns
        for i in range(9):
            nums = set()
            for j in range(9):
                cell = board[j][i]
                if cell != "." and cell in nums:
                    print(f"Failing column check at {i}{j}")
                    return False
                else:
                    nums.add(cell)

        # Check sub-boxes
        sub_boxes = [
            (0,0),
            (0,3),
            (0,6),
            (3,0),
            (3,3),
            (3,6),
            (6,0),
            (6,3),
            (6,6),
        ]

        for row, col in sub_boxes:
            if not self.sub_box_is_valid(board, row, col):
                print(f"Failing sub-box check at {row}, {col}")
                return False

        return True