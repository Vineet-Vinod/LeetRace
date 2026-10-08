class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        positions = [0] * (rows * cols + 1)
        for row in range(rows):
            for col in range(cols):
                positions[mat[row][col]] = row * cols + col
        painted_rows, painted_cols = [0] * rows, [0] * cols
        for index, value in enumerate(arr):
            position = positions[value]
            row, col = divmod(position, cols)
            painted_rows[row] += 1
            painted_cols[col] += 1
            if painted_rows[row] == cols or painted_cols[col] == rows:
                return index
        return -1
