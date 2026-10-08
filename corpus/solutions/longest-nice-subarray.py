class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        used_bits = 0
        longest = 0
        for right, value in enumerate(nums):
            while used_bits & value:
                used_bits ^= nums[left]
                left += 1
            used_bits |= value
            longest = max(longest, right - left + 1)
        return longest
