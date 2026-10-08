class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        powers = set()
        value = 1
        while value <= 2 ** len(s):
            powers.add(bin(value)[2:])
            value *= 5
        n = len(s)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for end in range(1, n + 1):
            for start in range(end):
                piece = s[start:end]
                if piece in powers:
                    dp[end] = min(dp[end], dp[start] + 1)
        return dp[n] if dp[n] <= n else -1
