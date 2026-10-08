class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        size = len(nums)
        total = sum(nums)
        current = sum(index * value for index, value in enumerate(nums))
        best = current
        for _ in range(1, size):
            current += total - size * nums[-_]
            best = max(best, current)
        return best
