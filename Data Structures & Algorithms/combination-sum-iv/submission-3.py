class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def helper(remaining: int) -> int:
            if remaining < 0:
                return 0
            if remaining == 0:
                return 1
            if remaining in memo:
                return memo[remaining]
            
            result = 0
            for num in nums:
                result += helper(remaining - num)
            
            memo[remaining] = result
            return result
        
        return helper(target)
