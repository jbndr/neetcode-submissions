class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr2 = arr[:]

        for i in range(len(arr)):
            arr2[i] = (abs(arr[i]-x), arr[i])

        arr2.sort()

        print(arr2)

        arr2 = arr2[:k]

        result = [val for diff, val in arr2]

        result.sort()

        return result