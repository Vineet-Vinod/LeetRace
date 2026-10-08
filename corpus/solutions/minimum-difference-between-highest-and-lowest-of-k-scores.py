class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        ordered = sorted(nums)
        return min(
            ordered[index + k - 1] - ordered[index]
            for index in range(len(nums) - k + 1)
        )
