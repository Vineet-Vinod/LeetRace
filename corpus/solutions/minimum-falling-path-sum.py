class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        previous = matrix[0][:]
        for row in matrix[1:]:
            current = []
            for col, value in enumerate(row):
                current.append(
                    value + min(previous[max(0, col - 1) : min(len(row), col + 2)])
                )
            previous = current
        return min(previous)
