class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        size = len(grid)
        island = []
        found = False
        for row in range(size):
            if found:
                break
            for col in range(size):
                if grid[row][col] == 1:
                    stack = [(row, col)]
                    grid[row][col] = 2
                    while stack:
                        current_row, current_col = stack.pop()
                        island.append((current_row, current_col))
                        for nr, nc in (
                            (current_row + 1, current_col),
                            (current_row - 1, current_col),
                            (current_row, current_col + 1),
                            (current_row, current_col - 1),
                        ):
                            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                stack.append((nr, nc))
                    found = True
                    break
        queue = deque((row, col, 0) for row, col in island)
        while queue:
            row, col, distance = queue.popleft()
            for nr, nc in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if 0 <= nr < size and 0 <= nc < size:
                    if grid[nr][nc] == 1:
                        return distance
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, distance + 1))
        return -1
