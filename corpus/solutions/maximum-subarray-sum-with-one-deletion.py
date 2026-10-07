class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        kept = arr[0]
        deleted = float("-inf")
        best = arr[0]
        for value in arr[1:]:
            deleted = max(kept, deleted + value)
            kept = max(value, kept + value)
            best = max(best, kept, deleted)
        return best
