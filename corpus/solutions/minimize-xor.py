class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits_needed = num2.bit_count()
        result = 0
        for bit in range(31, -1, -1):
            if bits_needed and num1 & (1 << bit):
                result |= 1 << bit
                bits_needed -= 1
        for bit in range(32):
            if bits_needed and not result & (1 << bit):
                result |= 1 << bit
                bits_needed -= 1
        return result
