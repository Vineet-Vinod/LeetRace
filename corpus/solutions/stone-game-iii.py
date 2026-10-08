class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            total = 0
            best = -(10**30)
            for j in range(i, min(n, i + 3)):
                total += stoneValue[j]
                best = max(best, total - dp[j + 1])
            dp[i] = best
        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"
