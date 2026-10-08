class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        counts: dict[int, int] = {}
        left = best = 0
        for right, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1
            while counts[value] > k:
                counts[nums[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
