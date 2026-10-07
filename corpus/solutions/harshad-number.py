class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit_sum = sum(int(digit) for digit in str(x))
        return digit_sum if x % digit_sum == 0 else -1
