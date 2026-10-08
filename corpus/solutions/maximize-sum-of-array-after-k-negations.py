class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        values = sorted(nums)
        for i in range(min(k, len(values))):
            if values[i] < 0:
                values[i] = -values[i]
            else:
                break
        if k > sum(value < 0 for value in nums):
            if (k - sum(value < 0 for value in nums)) % 2:
                values[values.index(min(values))] *= -1
        return sum(values)
