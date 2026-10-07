class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * len(arr)
        for i in sorted(range(len(arr)), key=lambda i: arr[i]):
            for step in (-1, 1):
                for distance in range(1, d + 1):
                    j = i + distance * step
                    if not 0 <= j < len(arr) or arr[j] >= arr[i]:
                        break
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
