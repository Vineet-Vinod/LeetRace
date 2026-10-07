class Solution:
    def isGood(self, nums: list[int]) -> bool:
        maximum = len(nums) - 1
        return len(nums) == maximum + 1 and sorted(nums) == list(
            range(1, maximum + 1)
        ) + [maximum]
