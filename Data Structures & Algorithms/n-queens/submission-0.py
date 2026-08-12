class Solution:
    def isValidPlacement(self, board, r, c):
        return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]

        solutions = []

        def bp(state, row, blocked_cols, blocked_mdiag, blocked_adiag):
            if row == n:
                solutions.append(state.copy())
                return 

            for c in range(n):
                if c in blocked_cols or c-row in blocked_mdiag or c+row in blocked_adiag:
                    continue

                row_list = list(state[row])
                row_list[c] = "Q"
                state[row] = "".join(row_list)

                bp(state, row+1, 
                    blocked_cols | {c}, 
                    blocked_mdiag | {c-row}, 
                    blocked_adiag | {c+row})

                state[row] = "." * n

        bp(board, 0, set(), set(), set())

        return solutions