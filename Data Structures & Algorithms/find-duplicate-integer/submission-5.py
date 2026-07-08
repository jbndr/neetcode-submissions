class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) time, no extra space but modifiying array
        idx = 0

        while True:
            num = nums[idx]
            nums[idx] = 0
            if nums[num] == 0:
                return num
            idx = num