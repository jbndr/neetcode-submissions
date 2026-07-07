class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pairs.values():          # opening bracket
                stack.append(c)
            elif c in pairs:                 # closing bracket
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                return False                 # invalid character

        return not stack





