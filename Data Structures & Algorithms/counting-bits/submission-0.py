class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        i = 0

        while i <= n:
            result.append(bin(i).count("1"))
            i += 1

        return result
        