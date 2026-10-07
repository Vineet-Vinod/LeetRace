from typing import List
from math import isqrt


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        sieve = [True] * (isqrt(max(nums)) + 1)
        primes = []
        for p in range(2, len(sieve)):
            if sieve[p]:
                primes.append(p)
                for j in range(p * p, len(sieve), p):
                    sieve[j] = False
        factors = []
        last = {}
        for i, v in enumerate(nums):
            fs = []
            for p in primes:
                if p * p > v:
                    break
                if v % p == 0:
                    fs.append(p)
                    while v % p == 0:
                        v //= p
            if v > 1:
                fs.append(v)
            factors.append(fs)
            for p in fs:
                last[p] = i
        end = 0
        for i, fs in enumerate(factors[:-1]):
            for p in fs:
                end = max(end, last[p])
            if end == i:
                return i
        return -1
