class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        best = None
        for value in nums:
            prefix += value
            score = max(prefix, total - prefix + value)
            best = score if best is None else max(best, score)
        return best if best is not None else 0
