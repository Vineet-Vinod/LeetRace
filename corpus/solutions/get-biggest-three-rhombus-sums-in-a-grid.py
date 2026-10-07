class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        sums = set()
        for row in range(rows):
            for col in range(cols):
                sums.add(grid[row][col])
                radius = 1
                while (
                    row - radius >= 0
                    and row + radius < rows
                    and col - radius >= 0
                    and col + radius < cols
                ):
                    total = 0
                    for step in range(radius):
                        total += grid[row - radius + step][col + step]
                        total += grid[row + step][col + radius - step]
                        total += grid[row + radius - step][col - step]
                        total += grid[row - step][col - radius + step]
                    sums.add(total)
                    radius += 1
        return sorted(sums, reverse=True)[:3]
