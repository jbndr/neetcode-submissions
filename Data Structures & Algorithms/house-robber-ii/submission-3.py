class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [None] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        dp_without0 = [None] * (len(nums) + 1)
        dp_without0[0] = 0
        dp_without0[1] = nums[1] 

        for i in range(2, len(nums)):
            if i == len(nums)-1:
                dp[i] = max(nums[i], dp_without0[i-2]+nums[i], dp[i-1])
            else:  
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
                dp_without0[i] = max(nums[i]+dp_without0[i-2], dp_without0[i-1])

        return dp[len(nums)-1]