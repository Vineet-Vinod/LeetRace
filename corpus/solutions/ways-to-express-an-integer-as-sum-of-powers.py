class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        powers = []
        value = 1
        while value**x <= n:
            powers.append(value**x)
            value += 1
        ways = [0] * (n + 1)
        ways[0] = 1
        for power in powers:
            for total in range(n, power - 1, -1):
                ways[total] = (ways[total] + ways[total - power]) % mod
        return ways[n]
