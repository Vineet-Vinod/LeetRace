class Solution:
    def numSquares(self, n: int) -> int:
        root = isqrt(n)
        if root * root == n:
            return 1
        for first in range(1, isqrt(n) + 1):
            remainder = n - first * first
            second = isqrt(remainder)
            if second * second == remainder:
                return 2
        reduced = n
        while reduced % 4 == 0:
            reduced //= 4
        if reduced % 8 == 7:
            return 4
        return 3
