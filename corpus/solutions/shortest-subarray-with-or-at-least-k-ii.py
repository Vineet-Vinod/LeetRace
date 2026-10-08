class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = [0] * 31
        left = 0
        best = len(nums) + 1
        current_or = 0
        for right, value in enumerate(nums):
            for bit in range(31):
                if value >> bit & 1:
                    counts[bit] += 1
            current_or = 0
            for bit, count in enumerate(counts):
                if count:
                    current_or |= 1 << bit
            while left <= right and current_or >= k:
                best = min(best, right - left + 1)
                outgoing = nums[left]
                for bit in range(31):
                    if outgoing >> bit & 1:
                        counts[bit] -= 1
                left += 1
                current_or = 0
                for bit, count in enumerate(counts):
                    if count:
                        current_or |= 1 << bit
        return -1 if best > len(nums) else best
