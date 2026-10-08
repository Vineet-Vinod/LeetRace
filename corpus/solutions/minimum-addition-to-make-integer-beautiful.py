class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        original = n
        unit = 1
        while sum(int(digit) for digit in str(n)) > target:
            digit = n // unit % 10
            n += (10 - digit) % 10 * unit
            unit *= 10
        return n - original
