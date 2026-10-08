class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[10**18] * (k + 2) for _ in range(n + 1)]
        dp[0][0] = 0
        for end in range(1, n + 1):
            maximum = total = 0
            for start in range(end - 1, -1, -1):
                maximum = max(maximum, nums[start])
                total += nums[start]
                waste = maximum * (end - start) - total
                for operations in range(k + 1):
                    dp[end][operations + 1] = min(
                        dp[end][operations + 1], dp[start][operations] + waste
                    )
        return min(dp[n])
