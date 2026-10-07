class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        best = [0] * (k + 1)
        ending = {}
        for x in nums:
            dp = ending.setdefault(x, [0] * (k + 1))
            for changes in range(k, -1, -1):
                dp[changes] = max(
                    dp[changes] + 1, best[changes - 1] + 1 if changes else 1
                )
                best[changes] = max(best[changes], dp[changes])
        return best[k]
