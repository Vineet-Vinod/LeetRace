class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        if right >= 0:
            is_prime[0] = False
        if right >= 1:
            is_prime[1] = False
        for p in range(2, isqrt(right) + 1):
            if is_prime[p]:
                for multiple in range(p * p, right + 1, p):
                    is_prime[multiple] = False
        previous = -1
        best = [-1, -1]
        best_gap = right + 1
        for value in range(max(2, left), right + 1):
            if is_prime[value]:
                if previous != -1 and value - previous < best_gap:
                    best = [previous, value]
                    best_gap = value - previous
                previous = value
        return best
