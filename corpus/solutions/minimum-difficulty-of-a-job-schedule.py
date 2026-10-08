class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [0] + [10**9] * n
        for day in range(1, d + 1):
            nxt = [10**9] * (n + 1)
            for end in range(day, n + 1):
                hardest = 0
                for start in range(end - 1, day - 2, -1):
                    hardest = max(hardest, jobDifficulty[start])
                    nxt[end] = min(nxt[end], dp[start] + hardest)
            dp = nxt
        return dp[n]
