from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        nums.sort()

        def bt(path, candidates):
            solutions.append(path.copy())

            if len(nums) == len(path):
                return

            for idx, candidate in enumerate(candidates):
                if idx > 0 and candidates[idx-1] == candidate:
                    continue

                path.append(candidate)
                bt(path, candidates[idx+1:])
                path.pop()

        bt([], nums)

        return solutions


        