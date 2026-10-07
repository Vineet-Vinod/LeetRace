class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, width = len(strs), len(strs[0])
        ordered = [False] * (rows - 1)
        deletions = 0
        for col in range(width):
            if any(
                not ordered[row] and strs[row][col] > strs[row + 1][col]
                for row in range(rows - 1)
            ):
                deletions += 1
                continue
            for row in range(rows - 1):
                if strs[row][col] < strs[row + 1][col]:
                    ordered[row] = True
        return deletions
