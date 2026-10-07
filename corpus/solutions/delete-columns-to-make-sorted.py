class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(
            any(column[r] > column[r + 1] for r in range(len(strs) - 1))
            for column in zip(*strs)
        )
