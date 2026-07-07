class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        low = 0
        high = len(arr)

        while low < high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                high = mid
            else:
                low = mid + 1

        left = low - 1
        right = low

        while right-left-1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left]-x) <= abs(arr[right]-x):
                left -= 1
            else:
                right += 1

        return arr[left+1:right]



