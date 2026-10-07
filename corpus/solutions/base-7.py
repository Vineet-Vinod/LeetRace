class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        n = abs(num)
        digits = []
        while n:
            digits.append(str(n % 7))
            n //= 7
        return sign + "".join(reversed(digits))
