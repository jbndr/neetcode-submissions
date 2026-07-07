class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            pos = 1 << i
            if (n & pos):
                result += 1 << (31 - i)

        return result

        