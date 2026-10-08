class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        longest = 0
        for right, value in enumerate(nums):
            zeros += value == 0
            while zeros > k:
                zeros -= nums[left] == 0
                left += 1
            longest = max(longest, right - left + 1)
        return longest
