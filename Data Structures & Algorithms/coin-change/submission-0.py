class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            
            if amount < 0:
                return float("inf")
            
            if amount in memo:
                return memo[amount]

            answer = float("inf")

            for coin in coins:
                answer = min(answer, 1 + dp(amount-coin))

            memo[amount] = answer
            return answer

        result = dp(amount)

        if result == float('inf'):
            return -1

        return result

        
        