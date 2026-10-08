class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum((value >> bit) & 1 for value in candidates) for bit in range(24))
