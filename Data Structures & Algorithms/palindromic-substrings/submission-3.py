class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        count = 0

        for length in range(n):
            for i in range(n - length):
                j = i + length
                if length == 0:
                    dp[i][j] = True
                elif length == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

                if dp[i][j]:
                    count += 1
        
        return count