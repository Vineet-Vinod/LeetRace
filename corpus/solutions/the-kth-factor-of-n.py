class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        large = []
        for divisor in range(1, math.isqrt(n) + 1):
            if n % divisor == 0:
                small.append(divisor)
                if divisor * divisor != n:
                    large.append(n // divisor)
        factors = small + large[::-1]
        return factors[k - 1] if k <= len(factors) else -1
