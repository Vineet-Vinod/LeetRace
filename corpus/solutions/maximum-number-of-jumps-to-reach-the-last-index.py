class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        best = [-1] * len(nums)
        best[0] = 0
        for end in range(1, len(nums)):
            for start in range(end):
                if best[start] >= 0 and abs(nums[end] - nums[start]) <= target:
                    best[end] = max(best[end], best[start] + 1)
        return best[-1]
