from builtins import pow


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        q, r = divmod(primeFactors, 3)
        if r == 1:
            return pow(3, q - 1, 1000000007) * 4 % 1000000007
        return pow(3, q, 1000000007) * (2 if r == 2 else 1) % 1000000007
