class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        total = 0
        n = len(grid[0])
        for rows in (grid, grid[::-1]):
            previous = [0] * n
            for row in rows:
                current = row.copy()
                for j in range(1, n - 1):
                    if row[j]:
                        current[j] = 1 + min(previous[j - 1 : j + 2])
                        total += current[j] - 1
                previous = current
        return total
