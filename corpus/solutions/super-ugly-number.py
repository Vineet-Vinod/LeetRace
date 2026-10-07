class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        values = [1] * n
        indexes = [0] * len(primes)
        candidates = list(primes)
        for position in range(1, n):
            next_value = min(candidates)
            values[position] = next_value
            for i, prime in enumerate(primes):
                if candidates[i] == next_value:
                    indexes[i] += 1
                    candidates[i] = values[indexes[i]] * prime
        return values[-1]
