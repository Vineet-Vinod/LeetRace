class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for index in range(size):
            value = (nums[index] - 1) % size + 1
            nums[value - 1] += size
        return [
            index + 1 for index, value in enumerate(nums) if (value - 1) // size == 2
        ]
