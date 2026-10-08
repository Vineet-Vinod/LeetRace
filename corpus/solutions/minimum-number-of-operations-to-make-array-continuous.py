class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        values = sorted(set(nums))
        left = best = 0
        for right, x in enumerate(values):
            while x - values[left] >= n:
                left += 1
            best = max(best, right - left + 1)
        return n - best
