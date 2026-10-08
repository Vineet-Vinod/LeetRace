class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [0.0] * (target + 1)
        dp[0] = 1.0
        for probability in prob:
            for heads in range(target, -1, -1):
                stay = dp[heads] * (1.0 - probability)
                gain = dp[heads - 1] * probability if heads else 0.0
                dp[heads] = stay + gain
        return dp[target]
