class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        max_len = 0
        start_index = 0

        for length in range(n):
            for i in range(n - length):
                j = i + length
                if length == 0:
                    dp[i][j] = True
                elif length == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    start_index = i
        
        return s[start_index:start_index+max_len]