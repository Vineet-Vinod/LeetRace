class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            counts = [0] * 26
            minimum = 0
            maximum = 0
            for start in range(end - 1, -1, -1):
                index = ord(s[start]) - ord("a")
                counts[index] += 1
                minimum = min((value for value in counts if value), default=0)
                maximum = max(counts)
                if minimum == maximum:
                    dp[end] = min(dp[end], dp[start] + 1)
        return dp[n]
