from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        n = len(nums)
        nums.sort()

        def bt(path, start):
            solutions.append(path.copy())

            if len(nums) == len(path):
                return

            for idx in range(start, n):
                candidate = nums[idx]
                if idx > start and nums[idx-1] == candidate:
                    continue

                path.append(candidate)
                bt(path, idx+1)
                path.pop()

        bt([], 0)

        return solutions


        