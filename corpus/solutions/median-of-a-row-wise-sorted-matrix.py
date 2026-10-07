class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        low = min(row[0] for row in grid)
        high = max(row[-1] for row in grid)
        target = rows * cols // 2 + 1
        while low < high:
            middle = (low + high) // 2
            count = sum(bisect_right(row, middle) for row in grid)
            if count < target:
                low = middle + 1
            else:
                high = middle
        return low
