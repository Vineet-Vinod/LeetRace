from typing import List
from math import isqrt


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        maximum = max(nums)
        parent = list(range(maximum + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        primes = []
        sieve = [True] * (isqrt(maximum) + 1)
        for p in range(2, len(sieve)):
            if sieve[p]:
                primes.append(p)
                for j in range(p * p, len(sieve), p):
                    sieve[j] = False
        for v in set(nums):
            x = v
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    parent[find(v)] = find(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                parent[find(v)] = find(x)
        return all(find(a) == find(b) for a, b in zip(nums, sorted(nums)))
