from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        freq = Counter(nums)

        for num, count in freq.items():
            if count > 1:
                return num