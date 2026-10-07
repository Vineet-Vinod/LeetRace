from builtins import pow


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        if sum(nums) < 2 * k:
            return 0
        dp = [0] * k
        dp[0] = 1
        for x in nums:
            for total in range(k - 1, x - 1, -1):
                dp[total] = (dp[total] + dp[total - x]) % mod
        return (pow(2, len(nums), mod) - 2 * sum(dp)) % mod
