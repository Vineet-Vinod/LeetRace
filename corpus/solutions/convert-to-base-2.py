class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n:
            n, remainder = divmod(n, -2)
            if remainder < 0:
                remainder += 2
                n += 1
            digits.append(str(remainder))
        return "".join(reversed(digits))
