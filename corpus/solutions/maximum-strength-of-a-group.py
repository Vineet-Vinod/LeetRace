class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        best = None
        for mask in range(1, 1 << len(nums)):
            product = 1
            for index, value in enumerate(nums):
                if mask & (1 << index):
                    product *= value
            best = product if best is None else max(best, product)
        return best if best is not None else 0
