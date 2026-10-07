class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        longest = 0
        for value in values:
            if value - 1 not in values:
                end = value
                while end in values:
                    end += 1
                longest = max(longest, end - value)
        return longest
