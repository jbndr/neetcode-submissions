class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0 
        r = m*n

        while l < r:
            mid = l + ((r-l)//2)

            row = mid // n
            col = mid - (row*n)

            if matrix[row][col] >= target:
                r = mid
            else:
                l = mid + 1


        row = l // n
        col = l - (row*n)

        if l < m*n and matrix[row][col] == target:
            return True

        return False