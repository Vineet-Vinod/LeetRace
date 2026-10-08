class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    grid[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
                )
                if prefix[r + 1][c + 1] <= k:
                    count += 1
        return count
