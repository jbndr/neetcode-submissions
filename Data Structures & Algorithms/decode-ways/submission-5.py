class Solution:
    def numDecodings(self, s: str) -> int:
        chars = [str(i) for i in range(1, 27)]

        memo = {}

        def dp(i):
            if s[i:].startswith("0"):
                return 0

            if i >= len(s):
                return 1

            if i not in memo:
                matches = 0
                for c in chars:
                    if s[i:].startswith(c):
                        suffix_matches = dp(i+len(c))
                        if suffix_matches != -1:
                            matches += suffix_matches
                memo[i] = matches

            return memo[i]

        return dp(0)
        
        