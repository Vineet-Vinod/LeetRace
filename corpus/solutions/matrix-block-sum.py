class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                prefix[row + 1][col + 1] = (
                    mat[row][col]
                    + prefix[row][col + 1]
                    + prefix[row + 1][col]
                    - prefix[row][col]
                )
        result = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                top, bottom = max(0, row - k), min(rows, row + k + 1)
                left, right = max(0, col - k), min(cols, col + k + 1)
                result[row][col] = (
                    prefix[bottom][right]
                    - prefix[top][right]
                    - prefix[bottom][left]
                    + prefix[top][left]
                )
        return result
