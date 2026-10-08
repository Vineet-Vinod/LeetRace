class Solution:
    def canReachCorner(
        self, xCorner: int, yCorner: int, circles: List[List[int]]
    ) -> bool:
        n = len(circles)
        parent = list(range(n + 2))

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def join(i, j):
            parent[find(i)] = find(j)

        for i, (x, y, r) in enumerate(circles):
            if (
                x * x + y * y <= r * r
                or (x - xCorner) ** 2 + (y - yCorner) ** 2 <= r * r
            ):
                return False
            # Distance to each finite boundary segment, using integer arithmetic.
            left = x * x + max(0, y - yCorner) ** 2 <= r * r
            top = (y - yCorner) ** 2 + max(0, x - xCorner) ** 2 <= r * r
            bottom = y * y + max(0, x - xCorner) ** 2 <= r * r
            right = (x - xCorner) ** 2 + max(0, y - yCorner) ** 2 <= r * r
            if left or top:
                join(i, n)
            if bottom or right:
                join(i, n + 1)
            for j in range(i):
                u, v, t = circles[j]
                if (
                    (x - u) ** 2 + (y - v) ** 2 <= (r + t) ** 2
                    and x * t + u * r < xCorner * (r + t)
                    and y * t + v * r < yCorner * (r + t)
                ):
                    join(i, j)
            if find(n) == find(n + 1):
                return False
        return True
