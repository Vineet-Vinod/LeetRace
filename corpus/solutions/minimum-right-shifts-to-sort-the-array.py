class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        drops = [i for i in range(len(nums) - 1) if nums[i] > nums[i + 1]]
        if not drops:
            return 0
        if len(drops) == 1 and nums[-1] <= nums[0]:
            return len(nums) - drops[0] - 1
        return -1
