class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r, c) in seen:
                    continue
                area = 0
                stack = [(r, c)]
                seen.add((r, c))
                while stack:
                    row, col = stack.pop()
                    area += 1
                    for nr, nc in (
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    ):
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                best = max(best, area)
        return best
