class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = [0] * 32
        left = 0
        best = len(nums) + 1
        current_or = 0
        for right, value in enumerate(nums):
            for bit in range(32):
                if value & (1 << bit):
                    counts[bit] += 1
                    current_or |= 1 << bit
            while left <= right and current_or >= k:
                best = min(best, right - left + 1)
                removed = nums[left]
                for bit in range(32):
                    if removed & (1 << bit):
                        counts[bit] -= 1
                        if counts[bit] == 0:
                            current_or &= ~(1 << bit)
                left += 1
        return -1 if best == len(nums) + 1 else best
