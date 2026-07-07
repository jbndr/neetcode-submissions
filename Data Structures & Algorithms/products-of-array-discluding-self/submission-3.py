class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for idx, val in enumerate(nums):
            output[idx] = prefix
            prefix *= nums[idx]
        
        suffix = 1
        for idx, val in reversed(list(enumerate(nums))):
            output[idx] *= suffix
            suffix *= nums[idx]

        return output
        