class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        right = [[0] * (cols + 1) for _ in range(rows)]
        down = [[0] * cols for _ in range(rows + 1)]
        best = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if grid[r][c]:
                    right[r][c] = 1 + right[r][c + 1]
                    down[r][c] = 1 + down[r + 1][c]
                    size = min(right[r][c], down[r][c])
                    while size > best:
                        if (
                            down[r][c + size - 1] >= size
                            and right[r + size - 1][c] >= size
                        ):
                            best = size
                            break
                        size -= 1
        return best * best
