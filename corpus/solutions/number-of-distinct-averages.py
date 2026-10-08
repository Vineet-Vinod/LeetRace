class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        values = sorted(nums)
        sums = {values[i] + values[-1 - i] for i in range(len(values) // 2)}
        return len(sums)
