class Solution:
    def tribonacci(self, n: int) -> int:
        values = (0, 1, 1)
        if n < 3:
            return values[n]
        first, second, third = values
        for _ in range(3, n + 1):
            first, second, third = second, third, first + second + third
        return third
