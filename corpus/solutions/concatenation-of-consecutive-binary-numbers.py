class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulus = 1_000_000_007
        result = 0
        bit_length = 0
        for value in range(1, n + 1):
            if value & (value - 1) == 0:
                bit_length += 1
            result = ((result << bit_length) | value) % modulus
        return result
