class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        total = 10
        choices = 9
        for digits in range(2, n + 1):
            choices *= 11 - digits
            total += choices
        return total
