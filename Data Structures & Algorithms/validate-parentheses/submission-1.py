class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for c in s:
            print(c)
            if c in ["{", "(", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                last = stack.pop()
                
                if last != pairs[c]:
                    return False

        return len(stack) == 0





