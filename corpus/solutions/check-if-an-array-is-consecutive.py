class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums) and max(nums) - min(nums) == len(nums) - 1
