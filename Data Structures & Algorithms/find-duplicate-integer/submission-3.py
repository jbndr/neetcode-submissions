class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(nlogn) time, O(1) space
        nums.sort()

        for idx, num in enumerate(nums):
            if nums[idx] == nums[idx+1]:
                return num