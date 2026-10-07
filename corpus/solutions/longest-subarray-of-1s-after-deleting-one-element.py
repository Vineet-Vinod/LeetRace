class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        longest = 0
        for right, value in enumerate(nums):
            zeros += value == 0
            while zeros > 1:
                zeros -= nums[left] == 0
                left += 1
            longest = max(longest, right - left)
        return longest
