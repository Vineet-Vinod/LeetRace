class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mod = 10**9 + 7
        dp = [1]
        for ch in s:
            length = len(dp)
            nxt = [0] * (length + 1)
            running = 0
            if ch == "I":
                for rank in range(length + 1):
                    nxt[rank] = running
                    if rank < length:
                        running = (running + dp[rank]) % mod
            else:
                for rank in range(length, -1, -1):
                    nxt[rank] = running
                    if rank:
                        running = (running + dp[rank - 1]) % mod
            dp = nxt
        return sum(dp) % mod
