class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        start = next(
            (r, c) for r in range(rows) for c in range(columns) if grid[r][c] == "*"
        )
        queue = deque([(start[0], start[1], 0)])
        seen = {start}
        while queue:
            row, column, distance = queue.popleft()
            if grid[row][column] == "#":
                return distance
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < columns
                    and grid[nr][nc] != "X"
                    and (nr, nc) not in seen
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc, distance + 1))
        return -1
