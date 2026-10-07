class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = sum(
            nums[index] > nums[(index + 1) % len(nums)] for index in range(len(nums))
        )
        return drops <= 1
