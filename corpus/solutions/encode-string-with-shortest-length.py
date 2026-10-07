class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [[""] * (n + 1) for _ in range(n)]

        def key(x: str) -> tuple[int, str]:
            return len(x), x

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length
                raw = s[i:j]
                best = raw
                for mid in range(i + 1, j):
                    candidate = dp[i][mid] + dp[mid][j]
                    if key(candidate) < key(best):
                        best = candidate
                for period in range(1, length // 2 + 1):
                    if length % period == 0 and raw == raw[:period] * (
                        length // period
                    ):
                        candidate = (
                            str(length // period) + "[" + dp[i][i + period] + "]"
                        )
                        if len(candidate) < length and key(candidate) < key(best):
                            best = candidate
                # An uncompressed substring wins if compression does not shorten it.
                dp[i][j] = raw if len(best) == length else best
        return dp[0][n]
