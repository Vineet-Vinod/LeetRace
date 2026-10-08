class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        board = [row[:] for row in grid]
        for r, c in hits:
            board[r][c] = 0
        roof = m * n
        parent = list(range(roof + 1))
        size = [1] * (roof + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            a, b = find(a), find(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        def connect(r: int, c: int) -> None:
            if r == 0:
                union(r * n + c, roof)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < m and 0 <= cc < n and board[rr][cc]:
                    union(r * n + c, rr * n + cc)

        for r in range(m):
            for c in range(n):
                if board[r][c]:
                    connect(r, c)
        out = []
        for r, c in reversed(hits):
            if not grid[r][c]:
                out.append(0)
                continue
            before = size[find(roof)]
            board[r][c] = 1
            connect(r, c)
            out.append(max(0, size[find(roof)] - before - 1))
        return out[::-1]
