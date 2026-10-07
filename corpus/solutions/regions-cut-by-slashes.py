class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first: int, second: int) -> None:
            parent[find(first)] = find(second)

        for r in range(n):
            for c in range(n):
                cell = 4 * (r * n + c)
                char = grid[r][c]
                if char == " ":
                    union(cell, cell + 1)
                    union(cell + 1, cell + 2)
                    union(cell + 2, cell + 3)
                elif char == "/":
                    union(cell, cell + 3)
                    union(cell + 1, cell + 2)
                else:
                    union(cell, cell + 1)
                    union(cell + 2, cell + 3)
                if r > 0:
                    union(cell, cell - 4 * n + 2)
                if c > 0:
                    union(cell + 3, cell - 4 + 1)
        return len({find(i) for i in range(4 * n * n)})
