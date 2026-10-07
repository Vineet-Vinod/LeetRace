class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        for layer in range(min(rows, cols) // 2):
            cells: list[tuple[int, int]] = []
            top, left = layer, layer
            bottom, right = rows - 1 - layer, cols - 1 - layer
            cells.extend((top, c) for c in range(left, right + 1))
            cells.extend((r, right) for r in range(top + 1, bottom + 1))
            cells.extend((bottom, c) for c in range(right - 1, left - 1, -1))
            cells.extend((r, left) for r in range(bottom - 1, top, -1))
            shift = k % len(cells)
            values = [grid[r][c] for r, c in cells]
            for i, (r, c) in enumerate(cells):
                grid[r][c] = values[(i + shift) % len(cells)]
        return grid
