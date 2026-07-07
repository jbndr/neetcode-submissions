class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, choices):
            print(path)
            if sum(path) == target:
                result.append(path[:])
                return

            for idx, choice in enumerate(choices):
                if sum(path) + choice > target:
                    continue

                path.append(choice)
                backtrack(path, choices[idx:])
                path.pop()

        backtrack([], nums)

        return result

