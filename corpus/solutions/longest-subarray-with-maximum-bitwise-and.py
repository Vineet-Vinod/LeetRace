class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        best = run = 0
        for value in nums:
            if value == maximum:
                run += 1
                best = max(best, run)
            else:
                run = 0
        return best
