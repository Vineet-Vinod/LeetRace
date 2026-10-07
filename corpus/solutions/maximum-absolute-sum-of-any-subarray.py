class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minimum_prefix = 0
        maximum_prefix = 0
        prefix = 0
        best = 0
        for value in nums:
            prefix += value
            best = max(best, prefix - minimum_prefix, maximum_prefix - prefix)
            minimum_prefix = min(minimum_prefix, prefix)
            maximum_prefix = max(maximum_prefix, prefix)
        return best
