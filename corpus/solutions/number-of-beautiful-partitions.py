class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        prime = set("2357")
        n = len(s)
        if s[0] not in prime or s[-1] in prime or k * minLength > n:
            return 0
        dp = [1] + [0] * n
        for _ in range(k):
            next_dp = [0] * (n + 1)
            running = 0
            for end in range(1, n + 1):
                start = end - minLength
                if start >= 0 and s[start] in prime:
                    running = (running + dp[start]) % (10**9 + 7)
                if s[end - 1] not in prime:
                    next_dp[end] = running
            dp = next_dp
        return dp[n]
