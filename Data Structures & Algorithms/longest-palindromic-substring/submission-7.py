class Solution:
    def isPalindrome(self, s):
        return s[::-1] == s

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = float("-inf")
        start, end = None, None

        for i in range(n):
            for j in range(n):
                if self.isPalindrome(s[i:j+1]):
                    if j-i+1 > max_len:
                        max_len = max(max_len, j-i+1)
                        start = i
                        end = j

        return s[start:end+1]

