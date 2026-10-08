class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = set(range(1, n + 1))
        return all(set(row) == target for row in matrix) and all(
            {matrix[r][c] for r in range(n)} == target for c in range(n)
        )
