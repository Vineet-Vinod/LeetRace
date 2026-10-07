class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        flips = 0
        for row in range(rows // 2):
            for col in range(cols // 2):
                ones = (
                    grid[row][col]
                    + grid[rows - 1 - row][col]
                    + grid[row][cols - 1 - col]
                    + grid[rows - 1 - row][cols - 1 - col]
                )
                flips += min(ones, 4 - ones)
        paired_ones = mismatched_pairs = 0
        if rows % 2:
            row = rows // 2
            for col in range(cols // 2):
                first, second = grid[row][col], grid[row][cols - 1 - col]
                paired_ones += first + second == 2
                mismatched_pairs += first != second
        if cols % 2:
            col = cols // 2
            for row in range(rows // 2):
                first, second = grid[row][col], grid[rows - 1 - row][col]
                paired_ones += first + second == 2
                mismatched_pairs += first != second
        flips += mismatched_pairs
        if rows % 2 and cols % 2:
            flips += grid[rows // 2][cols // 2]
        if paired_ones % 2 and mismatched_pairs == 0:
            flips += 2
        return flips
