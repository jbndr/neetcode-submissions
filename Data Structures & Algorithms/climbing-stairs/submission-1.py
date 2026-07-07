class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(k):
            if k == 1:
                return 1
            
            if k == 2:
                return 2

            if k in memo:
                return memo[k]

            memo[k] = dp(k-1) + dp(k-2)
            return memo[k]

        return dp(n)