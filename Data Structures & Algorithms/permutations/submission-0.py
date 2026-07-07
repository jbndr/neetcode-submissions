class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        n = len(nums)

        def backtrack(path, choices):
            if len(path) == n:
                result.append(path.copy())
                return

            for choice in choices:
                path.append(choice)
                backtrack(path, [c for c in choices if c != choice])
                path.pop()

        backtrack([], nums)

        return result
        