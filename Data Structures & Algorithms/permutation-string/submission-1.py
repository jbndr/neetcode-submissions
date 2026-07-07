from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0

        pattern = Counter(s1)

        window = ""

        for right in range(len(s2)):
            window += s2[right]

            if Counter(window) == pattern:
                return True

            if len(window) == k:
                window = window[1:]

        
        return False


        