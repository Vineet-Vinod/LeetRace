class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        lowest = nums[0]
        best = -1
        for value in nums[1:]:
            if value > lowest:
                best = max(best, value - lowest)
            lowest = min(lowest, value)
        return best
