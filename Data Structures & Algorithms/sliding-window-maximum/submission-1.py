from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums)-k+1)
        state = deque(nums[:k-1])

        # O(n*k)
        for right in range(k-1, len(nums)):
            state.append(nums[right])
            result[right-k+1] = max(state)
            state.popleft()

        return result
        