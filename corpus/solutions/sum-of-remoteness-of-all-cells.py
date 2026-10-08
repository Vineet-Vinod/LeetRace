class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen: set[tuple[int, int]] = set()
        components: list[tuple[int, int]] = []
        total = sum(value for row in grid for value in row if value != -1)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == -1 or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                size = component_sum = 0
                while stack:
                    x, y = stack.pop()
                    size += 1
                    component_sum += grid[x][y]
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if (
                            0 <= nx < n
                            and 0 <= ny < n
                            and grid[nx][ny] != -1
                            and (nx, ny) not in seen
                        ):
                            seen.add((nx, ny))
                            stack.append((nx, ny))
                components.append((size, component_sum))
        return sum(size * (total - component_sum) for size, component_sum in components)
