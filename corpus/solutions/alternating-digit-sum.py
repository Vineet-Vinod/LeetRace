class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        return sum(
            (1 if i % 2 == 0 else -1) * int(digit) for i, digit in enumerate(digits)
        )
