class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = [True] * (n + 1)
        if n >= 0:
            prime[0] = False
        if n >= 1:
            prime[1] = False
        for value in range(2, math.isqrt(n) + 1):
            if prime[value]:
                for multiple in range(value * value, n + 1, value):
                    prime[multiple] = False
        return [
            [value, n - value]
            for value in range(2, n // 2 + 1)
            if prime[value] and prime[n - value]
        ]
