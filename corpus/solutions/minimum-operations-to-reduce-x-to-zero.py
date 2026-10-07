class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        left = current = best = 0
        for right, value in enumerate(nums):
            current += value
            while current > target and left <= right:
                current -= nums[left]
                left += 1
            if current == target:
                best = max(best, right - left + 1)
        return len(nums) - best if target >= 0 and (best or target == 0) else -1
