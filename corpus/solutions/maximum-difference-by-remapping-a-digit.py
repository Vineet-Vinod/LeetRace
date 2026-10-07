class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = str(num)
        high_digit = next((digit for digit in digits if digit != "9"), None)
        maximum = digits if high_digit is None else digits.replace(high_digit, "9")
        low_digit = digits[0]
        minimum = digits.replace(low_digit, "0")
        return int(maximum) - int(minimum)
