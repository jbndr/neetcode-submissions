class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(path, choices):
            result.append(path[:])

            for idx, choice in enumerate(choices):
                path.append(choice)
                backtrack(path, choices[idx+1:])
                path.pop()
            

        backtrack([], nums)

        return result