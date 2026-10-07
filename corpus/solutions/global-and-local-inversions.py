class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        maximum = -1
        for index in range(len(nums) - 2):
            maximum = max(maximum, nums[index])
            if maximum > nums[index + 2]:
                return False
        return True
