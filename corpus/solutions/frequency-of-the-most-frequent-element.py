class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        best = 1
        for right, value in enumerate(nums):
            total += value
            while value * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best
