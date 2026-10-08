class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        ordered = sorted(nums)
        return max(
            ordered[-1] * ordered[-2] * ordered[-3],
            ordered[0] * ordered[1] * ordered[-1],
        )
