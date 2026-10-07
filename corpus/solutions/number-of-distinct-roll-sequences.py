from math import gcd


class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6
        allowed = {
            (a, b): [c for c in range(1, 7) if c != a and c != b and gcd(b, c) == 1]
            for a in range(1, 7)
            for b in range(1, 7)
            if a != b and gcd(a, b) == 1
        }
        dp = {pair: 1 for pair in allowed}
        for _ in range(n - 2):
            nxt = {pair: 0 for pair in allowed}
            for (a, b), count in dp.items():
                for c in allowed[a, b]:
                    nxt[b, c] = (nxt[b, c] + count) % 1000000007
            dp = nxt
        return sum(dp.values()) % 1000000007
