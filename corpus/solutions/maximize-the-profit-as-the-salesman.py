class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        ending: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for start, end, gold in offers:
            ending[end].append((start, gold))
        dp = [0] * (n + 1)
        for end in range(n):
            dp[end + 1] = dp[end]
            for start, gold in ending[end]:
                dp[end + 1] = max(dp[end + 1], dp[start] + gold)
        return dp[n]
