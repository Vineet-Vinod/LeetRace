class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        seen = set()
        best = 0
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0 or (row, column) in seen:
                    continue
                total = 0
                stack = [(row, column)]
                seen.add((row, column))
                while stack:
                    current_row, current_column = stack.pop()
                    total += grid[current_row][current_column]
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = current_row + dr, current_column + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < columns
                            and grid[nr][nc] > 0
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                best = max(best, total)
        return best
