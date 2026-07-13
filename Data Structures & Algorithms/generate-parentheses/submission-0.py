class Solution:
    def isValid(self, sequence):
        stack = []

        for s in sequence:
            if s == "(":
                stack.append(")")
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val != s:
                    return False

        return len(stack) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        solutions = []
        
        def backtrack(path):
            if len(path) == 2*n:
                if self.isValid(path):
                    solutions.append(path)
                return

            for option in ["(", ")"]:
                old_path = path
                path += option
                backtrack(path)
                path = old_path

        backtrack("")

        return solutions