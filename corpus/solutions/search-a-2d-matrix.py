class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        low, high = 0, rows * columns
        while low < high:
            middle = (low + high) // 2
            value = matrix[middle // columns][middle % columns]
            if value < target:
                low = middle + 1
            else:
                high = middle
        return low < rows * columns and matrix[low // columns][low % columns] == target
