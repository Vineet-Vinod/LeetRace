class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)
        remainder = abs(dividend)
        denominator = abs(divisor)
        quotient = 0
        for shift in range(31, -1, -1):
            scaled = denominator << shift
            if scaled <= remainder:
                remainder -= scaled
                quotient |= 1 << shift
        if negative:
            quotient = -quotient
        return min(max(quotient, -(1 << 31)), (1 << 31) - 1)
