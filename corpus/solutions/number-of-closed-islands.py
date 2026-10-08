class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        closed = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    continue
                is_closed = True
                stack = [(r, c)]
                grid[r][c] = 1
                while stack:
                    row, col = stack.pop()
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        is_closed = False
                    for nr, nc in (
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    ):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            stack.append((nr, nc))
                closed += is_closed
        return closed
