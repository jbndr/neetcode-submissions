class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        min_dp = [float("inf") for _ in range(n)]
        max_dp = [float("-inf") for _ in range(n)]

        # base case
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]

        for i in range(1, n):
            # choices
            choices = [nums[i], min_dp[i-1]*nums[i], max_dp[i-1]*nums[i]]
            
            # transition
            min_dp[i] = min(choices)
            max_dp[i] = max(choices)

        answer = max_dp[0]
        for i in range(1, n):
            answer = max(answer, max_dp[i])

        return answer






        