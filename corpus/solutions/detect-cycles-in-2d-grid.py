class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        for start_row in range(rows):
            for start_col in range(cols):
                if visited[start_row][start_col]:
                    continue
                stack = [(start_row, start_col, -1, -1)]
                visited[start_row][start_col] = True
                while stack:
                    row, col, parent_row, parent_col = stack.pop()
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = row + dr, col + dc
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            continue
                        if grid[nr][nc] != grid[row][col] or (nr, nc) == (
                            parent_row,
                            parent_col,
                        ):
                            continue
                        if visited[nr][nc]:
                            return True
                        visited[nr][nc] = True
                        stack.append((nr, nc, row, col))
        return False
