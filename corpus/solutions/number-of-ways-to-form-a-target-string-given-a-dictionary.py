from collections import Counter


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        counts = [Counter(column) for column in zip(*words)]
        dp = [1] + [0] * len(target)
        for column in counts:
            for i in range(len(target) - 1, -1, -1):
                dp[i + 1] = (dp[i + 1] + dp[i] * column[target[i]]) % 1000000007
        return dp[-1]
