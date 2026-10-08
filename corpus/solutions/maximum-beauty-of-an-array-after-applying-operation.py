class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ordered = sorted(nums)
        left = best = 0
        for right, value in enumerate(ordered):
            while value - ordered[left] > 2 * k:
                left += 1
            best = max(best, right - left + 1)
        return best
