from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        shapes = set()
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c] or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                points = []
                while stack:
                    x, y = stack.pop()
                    points.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and grid[nx][ny]
                            and (nx, ny) not in seen
                        ):
                            seen.add((nx, ny))
                            stack.append((nx, ny))
                variants = []
                for swap in (False, True):
                    for sx in (-1, 1):
                        for sy in (-1, 1):
                            transformed = [
                                (sx * (y if swap else x), sy * (x if swap else y))
                                for x, y in points
                            ]
                            min_x = min(x for x, y in transformed)
                            min_y = min(y for x, y in transformed)
                            variants.append(
                                tuple(
                                    sorted(
                                        (x - min_x, y - min_y) for x, y in transformed
                                    )
                                )
                            )
                shapes.add(min(variants))
        return len(shapes)
