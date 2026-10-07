class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        current = 0
        best = 0
        for right, value in enumerate(nums):
            while value in seen:
                seen.remove(nums[left])
                current -= nums[left]
                left += 1
            seen.add(value)
            current += value
            best = max(best, current)
        return best
