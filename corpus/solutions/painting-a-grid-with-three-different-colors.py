from itertools import product


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        states = [
            p
            for p in product(range(3), repeat=m)
            if all(p[i] != p[i - 1] for i in range(1, m))
        ]
        neighbors = [
            [j for j, b in enumerate(states) if all(x != y for x, y in zip(a, b))]
            for a in states
        ]
        dp = [1] * len(states)
        mod = 10**9 + 7
        for _ in range(n - 1):
            dp = [sum(dp[j] for j in ns) % mod for ns in neighbors]
        return sum(dp) % mod
