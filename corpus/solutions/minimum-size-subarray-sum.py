class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        minimum = len(nums) + 1
        for right, value in enumerate(nums):
            total += value
            while total >= target:
                minimum = min(minimum, right - left + 1)
                total -= nums[left]
                left += 1
        return minimum if minimum <= len(nums) else 0
