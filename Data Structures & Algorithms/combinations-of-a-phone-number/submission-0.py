class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []

        if len(digits) == 0:
            return result

        def backtrack(idx, path):
            if len(path) == len(digits):
                result.append("".join(path[:]))
                return

            for option in map[digits[idx]]:
                path.append(option)
                backtrack(idx+1, path)
                path.pop()

        backtrack(0, [])

        return result