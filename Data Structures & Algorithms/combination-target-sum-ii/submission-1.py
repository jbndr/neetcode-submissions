class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()

        def backtrack(path, remaining_candidates, remaining_target):
            if remaining_target == 0:
                result.append(path.copy())
                return


            for idx, choice in enumerate(remaining_candidates):
                valid = choice <= remaining_target
                if not valid:
                    continue

                if idx > 0 and remaining_candidates[idx-1] == remaining_candidates[idx]:
                    continue

                next_choices = remaining_candidates[idx+1:]
                
                path.append(choice)
                backtrack(path, next_choices, remaining_target-choice)
                path.pop()

        backtrack([], candidates, target)

        return result

                
        