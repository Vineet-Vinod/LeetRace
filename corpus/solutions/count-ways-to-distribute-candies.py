from builtins import pow
from math import comb, factorial


class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        mod = 1000000007
        total = (
            sum(
                (-1 if (k - i) % 2 else 1) * comb(k, i) * pow(i, n, mod)
                for i in range(k + 1)
            )
            % mod
        )
        return total * pow(factorial(k) % mod, mod - 2, mod) % mod
