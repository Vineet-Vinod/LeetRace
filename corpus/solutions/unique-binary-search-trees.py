class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for nodes in range(1, n + 1):
            dp[nodes] = sum(dp[left] * dp[nodes - 1 - left] for left in range(nodes))
        return dp[n]
