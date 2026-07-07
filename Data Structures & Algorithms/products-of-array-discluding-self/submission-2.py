class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(len(nums)):
            for j, val in enumerate(nums):
                if i != j:
                    output[i] *= val

        return output


        