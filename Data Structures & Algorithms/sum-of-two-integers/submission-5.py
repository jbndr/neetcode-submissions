class Solution:
    def addBits(self, first: int, second: int, carry) -> (int, int):
        if not first and not second:
            return (carry,0)
        if first and second:
            return (carry, 1)
        if carry:
            return (0, 1)
        return (1, 0)
        
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # keep only 32 bits
        MAX  = 0x7FFFFFFF      # max positive signed 32-bit int

        result = 0
        carry = 0
        for i in range(32):
            position_mask = 1 << i
            res, carry = self.addBits(a & position_mask, b & position_mask, carry)

            if res:
                result |= position_mask

        if result > MAX:
            result = ~(result ^ MASK)

        return result
