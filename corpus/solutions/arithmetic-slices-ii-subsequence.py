from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [{} for _ in nums]
        answer = 0
        for i, value in enumerate(nums):
            for j in range(i):
                difference = value - nums[j]
                previous = dp[j].get(difference, 0)
                answer += previous
                dp[i][difference] = dp[i].get(difference, 0) + previous + 1
        return answer
