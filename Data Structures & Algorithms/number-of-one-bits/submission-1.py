class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        for i in range(32):
            shift = 1 << i
            if (shift & n):
                result += 1

        return result
