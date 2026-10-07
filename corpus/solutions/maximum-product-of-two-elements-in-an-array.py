class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = sorted(nums, reverse=True)[:2]
        return (first - 1) * (second - 1)
