class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_value = int(str(abs(x))[::-1]) * sign
        return reversed_value if -(2**31) <= reversed_value <= 2**31 - 1 else 0
