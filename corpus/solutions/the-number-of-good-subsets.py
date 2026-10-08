from collections import Counter
from builtins import pow
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        counts = Counter(nums)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dp = [1] + [0] * 1023
        for value in range(2, 31):
            if not counts[value] or any(
                value % (prime * prime) == 0 for prime in primes
            ):
                continue
            mask = sum(1 << i for i, prime in enumerate(primes) if value % prime == 0)
            for old in range(1023, -1, -1):
                if old & mask == 0:
                    dp[old | mask] = (dp[old | mask] + dp[old] * counts[value]) % mod
        return sum(dp[1:]) * pow(2, counts[1], mod) % mod
