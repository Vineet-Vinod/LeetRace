class Solution:
    def smallestNumber(self, n: int) -> str:
        if n == 1:
            return "1"
        digits = []
        for d in range(9, 1, -1):
            while n % d == 0:
                digits.append(str(d))
                n //= d
        if n > 1:
            return "-1"
        return "".join(reversed(digits))
