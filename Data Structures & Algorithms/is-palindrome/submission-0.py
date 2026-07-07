class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c.lower() for c in s if c.isalnum()])

        p1 = 0
        p2 = len(s)-1

        while 0 <= p1 <= p2 <= len(s)-1:
            if s[p1] != s[p2]:
                print(p1, p2, s[p1], s[p2])
                return False
            p1 += 1
            p2 -= 1

        return True
        