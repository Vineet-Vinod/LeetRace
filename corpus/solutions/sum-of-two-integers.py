class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        first, second = a & mask, b & mask
        while second:
            carry = ((first & second) << 1) & mask
            first = (first ^ second) & mask
            second = carry
        return first if first < 0x80000000 else ~(first ^ mask)
