class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])

        l = 0
        r = len(s)-1

        while 0 <= l <= r <= len(s)-1:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True
        