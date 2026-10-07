class Solution:
    def myPow(self, x: float, n: int) -> float:
        exponent = n
        if exponent < 0:
            x = 1.0 / x
            exponent = -exponent
        result = 1.0
        while exponent:
            if exponent % 2:
                result *= x
            x *= x
            exponent //= 2
        return result
