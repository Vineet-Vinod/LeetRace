class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:
        words = sentence.split()
        lengths = [len(word) for word in words]
        n = len(words)
        dp = [10**30] * (n + 1)
        dp[n] = 0
        for start in range(n - 1, -1, -1):
            row_length = 0
            for end in range(start, n):
                row_length += lengths[end] + (1 if end > start else 0)
                if row_length > k:
                    break
                cost = 0 if end == n - 1 else (k - row_length) ** 2
                dp[start] = min(dp[start], cost + dp[end + 1])
        return dp[0]
