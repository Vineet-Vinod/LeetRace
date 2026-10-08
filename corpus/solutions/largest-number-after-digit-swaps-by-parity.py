class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        for parity in (0, 1):
            positions = [
                i for i, digit in enumerate(digits) if int(digit) % 2 == parity
            ]
            ordered = sorted((digits[i] for i in positions), reverse=True)
            for i, digit in zip(positions, ordered):
                digits[i] = digit
        return int("".join(digits))
