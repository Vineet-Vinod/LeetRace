class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        result = []
        for diagonal in range(rows + cols - 1):
            values = []
            start_row = max(0, diagonal - cols + 1)
            end_row = min(rows - 1, diagonal)
            for row in range(start_row, end_row + 1):
                values.append(mat[row][diagonal - row])
            result.extend(values[::-1] if diagonal % 2 == 0 else values)
        return result
