class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = list(str(abs(num)))
        if num < 0:
            return -int("".join(sorted(digits, reverse=True)))
        digits.sort()
        first_nonzero = next(
            (index for index, digit in enumerate(digits) if digit != "0"), len(digits)
        )
        if first_nonzero == len(digits):
            return 0
        digits[0], digits[first_nonzero] = digits[first_nonzero], digits[0]
        return int("".join(digits))
