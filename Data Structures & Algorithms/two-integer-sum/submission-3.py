class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        numbers = {}

        for idx, num in enumerate(nums):
            if num in numbers:
                numbers[num].append(idx)
            else:
                numbers[num] = [idx]

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in numbers:
                for opt in numbers[diff]:
                    if opt != idx:
                        return [idx, opt]


        return []
        