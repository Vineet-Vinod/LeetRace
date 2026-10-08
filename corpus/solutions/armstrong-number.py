class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = str(n)
        power = len(digits)
        return sum(int(digit) ** power for digit in digits) == n
