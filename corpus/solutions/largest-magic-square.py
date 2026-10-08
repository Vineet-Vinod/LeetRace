class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        for size in range(min(rows, columns), 1, -1):
            for top in range(rows - size + 1):
                for left in range(columns - size + 1):
                    target = sum(grid[top][left : left + size])
                    if any(
                        sum(grid[row][left : left + size]) != target
                        for row in range(top + 1, top + size)
                    ):
                        continue
                    if any(
                        sum(grid[row][column] for row in range(top, top + size))
                        != target
                        for column in range(left, left + size)
                    ):
                        continue
                    if (
                        sum(grid[top + offset][left + offset] for offset in range(size))
                        != target
                    ):
                        continue
                    if (
                        sum(
                            grid[top + offset][left + size - offset - 1]
                            for offset in range(size)
                        )
                        != target
                    ):
                        continue
                    return size
        return 1
