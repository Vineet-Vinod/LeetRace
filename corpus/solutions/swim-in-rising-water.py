class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        while queue:
            time, row, column = heappop(queue)
            if row == n - 1 and column == n - 1:
                return time
            for a, b in [
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ]:
                if 0 <= a < n and 0 <= b < n and (a, b) not in visited:
                    visited.add((a, b))
                    heappush(queue, (max(time, grid[a][b]), a, b))
        return -1
