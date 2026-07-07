class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def canBreak(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]

            for word in wordDict:
                if s.startswith(word, start):
                    next_start = start+len(word)
                    if canBreak(next_start):
                        memo[start] = True
                        return True

            memo[start] = False
            return False

        return canBreak(0)
        








        