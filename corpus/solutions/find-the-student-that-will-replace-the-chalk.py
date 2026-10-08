class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remaining = k % sum(chalk)
        for index, required in enumerate(chalk):
            if remaining < required:
                return index
            remaining -= required
        return 0
