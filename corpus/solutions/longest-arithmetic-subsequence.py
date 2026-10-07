class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        lengths: list[dict[int, int]] = [{} for _ in nums]
        longest = 2
        for right in range(len(nums)):
            for left in range(right):
                difference = nums[right] - nums[left]
                lengths[right][difference] = lengths[left].get(difference, 1) + 1
                longest = max(longest, lengths[right][difference])
        return longest
