class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, choices):
            if sum(path) == target:
                path_copy = path[:]
                path_copy.sort()
                if path_copy not in result:
                    result.append(path_copy)
                return

            for choice in choices:
                if sum(path) + choice > target:
                    continue

                path.append(choice)
                backtrack(path, choices)
                path.pop()

        backtrack([], nums)

        return result

