class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            value = matrix[row][col]
            if value == target:
                return True
            if value > target:
                row -= 1
            else:
                col += 1
        return False
