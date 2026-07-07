from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0

        chars = defaultdict(int)

        for right in range(len(s)):
            chars[s[right]] += 1

            window = right - left + 1

            while len(chars.keys()) != window:
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1
                window = right - left + 1

            result = max(result, window)

            print(chars, result)
            
        return result
        