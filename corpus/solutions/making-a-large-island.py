class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        labels = [[0] * n for _ in range(n)]
        sizes = [0]
        for r in range(n):
            for c in range(n):
                if grid[r][c] and not labels[r][c]:
                    label = len(sizes)
                    labels[r][c] = label
                    stack = [(r, c)]
                    size = 0
                    while stack:
                        x, y = stack.pop()
                        size += 1
                        for u, v in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                            if (
                                0 <= u < n
                                and 0 <= v < n
                                and grid[u][v]
                                and not labels[u][v]
                            ):
                                labels[u][v] = label
                                stack.append((u, v))
                    sizes.append(size)
        answer = max(sizes)
        for r in range(n):
            for c in range(n):
                if not grid[r][c]:
                    neighbors = {
                        labels[x][y]
                        for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                        if 0 <= x < n and 0 <= y < n
                    }
                    answer = max(answer, 1 + sum(sizes[x] for x in neighbors))
        return answer
