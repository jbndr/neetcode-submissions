from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0

        pattern = Counter(s1)

        frequencies = defaultdict(int)

        for right in range(len(s2)):
            frequencies[s2[right]] += 1

            if frequencies == pattern:
                return True

            if right-left+1 == k:
                frequencies[s2[left]] -= 1
                if frequencies[s2[left]] == 0:
                    del frequencies[s2[left]]
                left += 1

        return False


        