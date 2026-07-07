from collections import defaultdict

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for i in range(len(nums)+1):
            if i not in count:
                return i
        