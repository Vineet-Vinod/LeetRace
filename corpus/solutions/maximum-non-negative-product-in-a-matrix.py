class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minimum = [[0] * cols for _ in range(rows)]
        maximum = [[0] * cols for _ in range(rows)]
        minimum[0][0] = maximum[0][0] = grid[0][0]
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                candidates: list[int] = []
                if row:
                    candidates.extend(
                        (
                            minimum[row - 1][col] * grid[row][col],
                            maximum[row - 1][col] * grid[row][col],
                        )
                    )
                if col:
                    candidates.extend(
                        (
                            minimum[row][col - 1] * grid[row][col],
                            maximum[row][col - 1] * grid[row][col],
                        )
                    )
                minimum[row][col] = min(candidates)
                maximum[row][col] = max(candidates)
        result = maximum[-1][-1]
        return result % 1_000_000_007 if result >= 0 else -1
