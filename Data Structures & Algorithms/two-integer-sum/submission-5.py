class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values_at_pos = {

        }

        for idx, num in enumerate(nums):
            values_at_pos[num] = idx

        for idx, num in enumerate(nums):
            if target - num in values_at_pos and values_at_pos[target-num] != idx:
                return [idx, values_at_pos[target-num]]
