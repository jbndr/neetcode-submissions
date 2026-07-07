from collections import Counter, defaultdict

class Solution:

    def is_lower(self, c: str):
        return ord(c) >= ord('a') and ord(c) <= ord('z')

    def is_valid(self, window, target):
        for key in target.keys():
            if window[key] < target[key]:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target = Counter(t)
        
        left = 0   
        start, end = 0,0

        min_window = float("inf")

        for right in range(len(s)):
            window = Counter(s[left:right+1])
            is_valid = self.is_valid(window, target)

            if not is_valid:
                continue
            else:
                if right-left+1 < min_window:
                    start = left
                    end = right
                    min_window = min(min_window, right-left+1)
            
            while is_valid:
                left += 1
                window = Counter(s[left:right+1])
                is_valid = self.is_valid(window, target)
                if is_valid:
                    if right-left+1 < min_window:
                        min_window = min(min_window, right-left+1)
                        start = left
                        end = right

        return "" if min_window == float("inf") else s[start:end+1]


        


        

        
            

            
        


        