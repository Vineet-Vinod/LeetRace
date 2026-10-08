class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = sum(
            all(value % divisor for divisor in range(2, int(value**0.5) + 1))
            for value in range(2, n + 1)
        )
        return factorial(primes) * factorial(n - primes) % (10**9 + 7)
