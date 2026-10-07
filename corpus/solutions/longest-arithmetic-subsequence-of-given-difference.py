class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengths: dict[int, int] = {}
        best = 0
        for value in arr:
            lengths[value] = lengths.get(value - difference, 0) + 1
            best = max(best, lengths[value])
        return best
