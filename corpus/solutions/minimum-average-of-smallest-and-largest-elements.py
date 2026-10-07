class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        values = sorted(nums)
        return min((values[i] + values[-1 - i]) / 2 for i in range(len(values) // 2))
