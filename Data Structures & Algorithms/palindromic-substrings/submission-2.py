class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j+1]):
                    count += 1

        return count
                

    def is_palindrome(self, s):
        return s == s[::-1]
        