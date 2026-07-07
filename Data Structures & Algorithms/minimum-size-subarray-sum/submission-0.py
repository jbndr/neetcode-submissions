class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = None
        left = 0

        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target and left <= right:
                if not minLen:
                    minLen = right-left+1
                else:
                    minLen = min(minLen, right-left+1)
                
                currSum -= nums[left]
                left += 1

        return minLen if minLen else 0


        