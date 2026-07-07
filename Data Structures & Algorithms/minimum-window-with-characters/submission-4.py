from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        target = Counter(t)
        required = len(target.keys())

        window = defaultdict(int)
        having = 0

        left = 0
        ans = (float('inf'), 0, 0) # window_length, start, end

        for right, char in enumerate(s):
            # 1. Expand to current state
            window[char] += 1
            if char in target and window[char] == target[char]:
                having += 1
            
            # 2. Shrink until invalid
            while left <= right and required == having:
                # Update best result
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                left_char = s[left]
                window[left_char] -= 1
                if left_char in target and target[left_char] > window[left_char]:
                    having -= 1

                left += 1
        
        length, start, end = ans
        return s[start:end+1] if length != float("inf") else ""
                


        