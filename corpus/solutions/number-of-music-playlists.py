class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for _ in range(goal):
            nxt = [0] * (n + 1)
            for used in range(1, n + 1):
                nxt[used] = (
                    dp[used - 1] * (n - used + 1) + dp[used] * max(0, used - k)
                ) % 1_000_000_007
            dp = nxt
        return dp[n]
