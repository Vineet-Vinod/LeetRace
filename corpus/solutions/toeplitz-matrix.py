class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(
            matrix[r][c] == matrix[r - 1][c - 1]
            for r in range(1, len(matrix))
            for c in range(1, len(matrix[0]))
        )
