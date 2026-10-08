class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        counts = Counter(value % space for value in nums)
        best_count = max(counts.values())
        return min(value for value in nums if counts[value % space] == best_count)
