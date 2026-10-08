class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        kept = 0
        deletions = 0
        i = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                deletions += 1
                i += 1
            else:
                kept += 2
                i += 2
        if i < len(nums):
            deletions += 1
        return deletions
