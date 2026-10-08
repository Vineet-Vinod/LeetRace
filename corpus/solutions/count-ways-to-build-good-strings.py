class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        ways = [0] * (high + 1)
        ways[0] = 1
        total = 0
        for length in range(1, high + 1):
            if length >= zero:
                ways[length] += ways[length - zero]
            if length >= one:
                ways[length] += ways[length - one]
            ways[length] %= mod
            if length >= low:
                total = (total + ways[length]) % mod
        return total
