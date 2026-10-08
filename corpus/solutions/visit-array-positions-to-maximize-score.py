class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        best = [float("-inf"), float("-inf")]
        parity = nums[0] % 2
        best[parity] = nums[0]
        for value in nums[1:]:
            p = value % 2
            best[p] = max(best[p] + value, best[1 - p] + value - x)
        return int(max(best))
