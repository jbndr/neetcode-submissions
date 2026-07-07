class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j - i
                max_area = max(max_area, width * min(heights[i], heights[j]))

        return max_area
            

        
        