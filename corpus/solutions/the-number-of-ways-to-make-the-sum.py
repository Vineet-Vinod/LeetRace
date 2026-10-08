class Solution:
    def numberOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        unrestricted = [0] * (n + 1)
        unrestricted[0] = 1
        for coin in (1, 2, 6):
            for total in range(coin, n + 1):
                unrestricted[total] = (
                    unrestricted[total] + unrestricted[total - coin]
                ) % mod

        return (
            sum(unrestricted[n - 4 * count] for count in range(min(2, n // 4) + 1))
            % mod
        )
