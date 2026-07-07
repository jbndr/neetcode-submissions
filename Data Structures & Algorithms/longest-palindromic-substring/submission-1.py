class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        m_i, m_j = 0, 0

        for i in range(len(s)+1):
            for j in range(len(s)+1):
                if self.isPalindrome(s[i:j]):
                    if j-i+1 > max_length:
                        max_length = j-i+1
                        m_i = i
                        m_j = j

        return s[m_i:m_j]

    def isPalindrome(self, s: str):
        return s == s[::-1]
        