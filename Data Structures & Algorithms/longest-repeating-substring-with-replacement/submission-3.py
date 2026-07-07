from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tokens = defaultdict(int)

        left = 0
        result = 0

        def is_invalid_window(s, tokens, left, right):
            return (right-left+1-max(tokens.values())) > k

        for right in range(len(s)):
            char = s[right]
            tokens[char] += 1

            while is_invalid_window(s, tokens, left, right):
                tokens[s[left]] -= 1
                if tokens[s[left]] == 0:
                    del tokens[s[left]]
                left += 1

            result = max(result, right-left+1)

        return result
                
            


