class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        costs = [float("inf")] * cols
        costs[0] = 0
        for row in range(rows):
            for col in range(cols):
                from_above = costs[col]
                from_left = costs[col - 1] if col else float("inf")
                costs[col] = min(from_above, from_left) + grid[row][col]
        return int(costs[-1])
