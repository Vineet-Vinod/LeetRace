class Solution:
    def countDigits(self, num: int) -> int:
        return sum(1 for digit in str(num) if num % int(digit) == 0)
