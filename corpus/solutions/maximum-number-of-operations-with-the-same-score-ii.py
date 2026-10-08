class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        targets = {nums[0] + nums[1], nums[0] + nums[-1], nums[-2] + nums[-1]}
        answer = 0
        for target in targets:
            dp = [[0] * n for _ in range(n)]
            for length in range(2, n + 1):
                for left in range(n - length + 1):
                    right = left + length - 1
                    best = 0
                    if nums[left] + nums[left + 1] == target:
                        best = 1 + (dp[left + 2][right] if left + 2 <= right else 0)
                    if nums[right - 1] + nums[right] == target:
                        best = max(
                            best, 1 + (dp[left][right - 2] if left <= right - 2 else 0)
                        )
                    if nums[left] + nums[right] == target:
                        best = max(
                            best,
                            1
                            + (dp[left + 1][right - 1] if left + 1 <= right - 1 else 0),
                        )
                    dp[left][right] = best
            answer = max(answer, dp[0][n - 1])
        return answer
