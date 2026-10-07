class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        ordered = sorted(nums)
        return min(ordered[-4 + moves] - ordered[moves] for moves in range(4))
