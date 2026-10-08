from builtins import pow


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        mod = 1000000007
        prefix = [0] * n
        j = 0
        for i in range(1, n):
            while j and t[i] != t[j]:
                j = prefix[j - 1]
            if t[i] == t[j]:
                j += 1
            prefix[i] = j
        matches = j = 0
        for char in s + s[:-1]:
            while j and char != t[j]:
                j = prefix[j - 1]
            if char == t[j]:
                j += 1
            if j == n:
                matches += 1
                j = prefix[j - 1]
        total = pow(n - 1, k, mod)
        sign = 1 if k % 2 == 0 else -1
        nonzero = (total - sign) * pow(n, mod - 2, mod) % mod
        return (matches * nonzero + (sign if s == t else 0)) % mod
