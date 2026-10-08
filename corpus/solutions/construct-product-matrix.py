class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        size = rows * cols
        result = [[0] * cols for _ in range(rows)]
        prefix = 1
        for index in range(size):
            row, col = divmod(index, cols)
            result[row][col] = prefix
            prefix = prefix * grid[row][col] % 12345
        suffix = 1
        for index in range(size - 1, -1, -1):
            row, col = divmod(index, cols)
            result[row][col] = result[row][col] * suffix % 12345
            suffix = suffix * grid[row][col] % 12345
        return result
