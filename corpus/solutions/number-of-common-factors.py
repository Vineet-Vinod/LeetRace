class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(
            a % value == 0 and b % value == 0 for value in range(1, min(a, b) + 1)
        )
