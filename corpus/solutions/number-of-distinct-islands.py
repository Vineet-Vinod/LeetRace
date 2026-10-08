class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        shapes: set[tuple[tuple[int, int], ...]] = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                shape = []
                stack = [(row, col)]
                grid[row][col] = 0
                while stack:
                    current_row, current_col = stack.pop()
                    shape.append((current_row - row, current_col - col))
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == 1
                        ):
                            grid[next_row][next_col] = 0
                            stack.append((next_row, next_col))
                shapes.add(tuple(sorted(shape)))
        return len(shapes)
