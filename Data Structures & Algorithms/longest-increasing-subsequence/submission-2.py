class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp(i) returns lis starting at i

        memo = {}

        def dp(i):
            if i == len(nums)-1:
                return 1

            if i not in memo:
                values = [1]
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        values.append(1 + dp(j))
                memo[i] = max(values)

            return memo[i]

        return max([dp(i) for i in range(len(nums))])
            

        
        