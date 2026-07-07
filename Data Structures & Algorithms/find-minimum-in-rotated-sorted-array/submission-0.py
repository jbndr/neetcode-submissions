class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        lo = 1 
        hi = len(nums)

        while lo <= hi:
            mid = lo + ((hi-lo) // 2)

            if nums[-mid % len(nums)] < minimum:
                minimum = nums[-mid % len(nums)]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return minimum



            