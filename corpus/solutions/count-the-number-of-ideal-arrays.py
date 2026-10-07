from math import comb


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        spf = list(range(maxValue + 1))
        for p in range(2, int(maxValue**0.5) + 1):
            if spf[p] == p:
                for v in range(p * p, maxValue + 1, p):
                    if spf[v] == v:
                        spf[v] = p
        result = 0
        mod = 10**9 + 7
        for v in range(1, maxValue + 1):
            ways = 1
            while v > 1:
                p = spf[v]
                power = 0
                while v % p == 0:
                    v //= p
                    power += 1
                ways = ways * comb(n + power - 1, power) % mod
            result = (result + ways) % mod
        return result
