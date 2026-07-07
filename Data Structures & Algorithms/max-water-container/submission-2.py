class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")

        l = 0
        r = len(heights) - 1

        while l < r:
            width = r - l
            max_area = max(max_area, width * min(heights[l], heights[r]))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return max_area
            

        
        