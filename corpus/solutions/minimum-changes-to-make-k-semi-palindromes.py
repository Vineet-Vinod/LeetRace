class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        costs = [[n] * (n + 1) for _ in range(n)]
        for length in range(2, n + 1):
            divisors = [d for d in range(1, length) if length % d == 0]
            for start in range(n - length + 1):
                best = n
                for d in divisors:
                    changes = 0
                    for offset in range(d):
                        left, right = start + offset, start + offset + length - d
                        while left < right:
                            changes += s[left] != s[right]
                            left += d
                            right -= d
                    best = min(best, changes)
                costs[start][start + length] = best
        dp = [n] * (n + 1)
        dp[0] = 0
        for parts in range(1, k + 1):
            nxt = [n] * (n + 1)
            for end in range(2 * parts, n + 1):
                nxt[end] = min(
                    dp[start] + costs[start][end]
                    for start in range(2 * (parts - 1), end - 1)
                )
            dp = nxt
        return dp[n]
