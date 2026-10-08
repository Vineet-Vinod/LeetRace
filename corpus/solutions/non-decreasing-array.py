class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for index in range(len(nums) - 1):
            if nums[index] <= nums[index + 1]:
                continue
            if changed:
                return False
            changed = True
            if index == 0 or nums[index - 1] <= nums[index + 1]:
                nums[index] = nums[index + 1]
            else:
                nums[index + 1] = nums[index]
        return True
