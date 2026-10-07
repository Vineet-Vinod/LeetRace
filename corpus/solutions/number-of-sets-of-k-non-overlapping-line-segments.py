class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        from math import comb

        return comb(n + k - 1, 2 * k) % mod
