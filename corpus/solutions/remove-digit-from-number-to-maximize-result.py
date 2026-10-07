class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i, char in enumerate(number):
            if char == digit and i + 1 < len(number) and number[i + 1] > digit:
                return number[:i] + number[i + 1 :]
        i = number.rfind(digit)
        return number[:i] + number[i + 1 :]
