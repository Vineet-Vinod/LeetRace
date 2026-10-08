class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1:
            return -1 if k % 2 else nums[0]
        candidates = nums[: min(len(nums), k - 1)]
        if k < len(nums):
            candidates.append(nums[k])
        return max(candidates, default=-1)
