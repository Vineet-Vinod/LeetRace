class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        median = ordered[len(nums) // 2]
        return sum(abs(value - median) for value in nums)
