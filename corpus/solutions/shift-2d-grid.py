class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        size = rows * cols
        flat = [x for row in grid for x in row]
        k %= size
        shifted = flat[-k:] + flat[:-k] if k else flat
        return [shifted[i * cols : (i + 1) * cols] for i in range(rows)]
