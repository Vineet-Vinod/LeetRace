class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num
        digits = []
        for digit in range(9, 1, -1):
            while num % digit == 0:
                digits.append(digit)
                num //= digit
        if num != 1:
            return 0
        result = int("".join(map(str, reversed(digits))))
        return result if result <= 2**31 - 1 else 0
