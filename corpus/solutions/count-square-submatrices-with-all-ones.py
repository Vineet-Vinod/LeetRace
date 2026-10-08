class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        total = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] and row and col:
                    matrix[row][col] += min(
                        matrix[row - 1][col],
                        matrix[row][col - 1],
                        matrix[row - 1][col - 1],
                    )
                total += matrix[row][col]
        return total
