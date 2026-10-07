class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = current = 1
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return longest
