from math import gcd


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        common = a * b // gcd(a, b)
        left, right = 1, n * min(a, b)
        while left < right:
            mid = (left + right) // 2
            if mid // a + mid // b - mid // common >= n:
                right = mid
            else:
                left = mid + 1
        return left % (10**9 + 7)
