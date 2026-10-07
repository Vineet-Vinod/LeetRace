from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        from collections import deque

        rows, cols = len(grid), len(grid[0])
        keys = {char for row in grid for char in row if char.islower()}
        full = (1 << len(keys)) - 1
        start = next(
            (i, j) for i in range(rows) for j in range(cols) if grid[i][j] == "@"
        )
        queue = deque([(start[0], start[1], 0, 0)])
        seen = {(start[0], start[1], 0)}
        while queue:
            x, y, mask, distance = queue.popleft()
            if mask == full:
                return distance
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue
                char = grid[nx][ny]
                if char == "#" or (
                    char.isupper() and not mask & (1 << (ord(char.lower()) - 97))
                ):
                    continue
                following = mask | (1 << (ord(char) - 97)) if char.islower() else mask
                state = (nx, ny, following)
                if state not in seen:
                    seen.add(state)
                    queue.append((nx, ny, following, distance + 1))
        return -1
