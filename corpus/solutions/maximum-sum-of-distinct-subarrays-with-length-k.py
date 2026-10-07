class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts = Counter()
        total = 0
        best = 0
        for right, value in enumerate(nums):
            counts[value] += 1
            total += value
            if right >= k:
                old = nums[right - k]
                counts[old] -= 1
                if counts[old] == 0:
                    del counts[old]
                total -= old
            if right >= k - 1 and len(counts) == k:
                best = max(best, total)
        return best
