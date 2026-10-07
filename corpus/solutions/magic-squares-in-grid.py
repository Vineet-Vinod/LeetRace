class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        for top in range(rows - 2):
            for left in range(cols - 2):
                values = [
                    grid[row][col]
                    for row in range(top, top + 3)
                    for col in range(left, left + 3)
                ]
                if set(values) != set(range(1, 10)):
                    continue
                if any(
                    sum(grid[row][col] for col in range(left, left + 3)) != 15
                    for row in range(top, top + 3)
                ):
                    continue
                if any(
                    sum(grid[row][col] for row in range(top, top + 3)) != 15
                    for col in range(left, left + 3)
                ):
                    continue
                if sum(grid[top + offset][left + offset] for offset in range(3)) != 15:
                    continue
                if (
                    sum(grid[top + offset][left + 2 - offset] for offset in range(3))
                    != 15
                ):
                    continue
                count += 1
        return count
