class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        x = 0
        for bit in range(n - 1, -1, -1):
            mask = 1 << bit
            a_bit, b_bit = bool(a & mask), bool(b & mask)
            if a_bit == b_bit:
                if not a_bit:
                    x |= mask
                continue
            first_prefix = (a ^ x) >> (bit + 1)
            second_prefix = (b ^ x) >> (bit + 1)
            if first_prefix <= second_prefix:
                x |= mask if not a_bit else 0
            else:
                x |= mask if not b_bit else 0
        return (a ^ x) * (b ^ x) % (10**9 + 7)
