class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = 0
        gain = 0
        high = -(10**6)
        low = 10**6
        for a, b in zip(nums, nums[1:]):
            difference = abs(a - b)
            base += difference
            gain = max(
                gain, abs(nums[0] - b) - difference, abs(nums[-1] - a) - difference
            )
            high = max(high, min(a, b))
            low = min(low, max(a, b))
        return base + max(gain, 2 * (high - low))
