from collections import defaultdict

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        target_sum = sum([i for i in range(len(nums)+1)])

        return target_sum - actual_sum
        