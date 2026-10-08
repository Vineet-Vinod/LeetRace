from collections import deque


class Solution:
    def minimumSeconds(self, land: list[list[str]]) -> int:
        m, n = len(land), len(land[0])
        flood = [[m * n + 1] * n for _ in range(m)]
        water = deque()
        start = (0, 0)
        for r in range(m):
            for c in range(n):
                if land[r][c] == "*":
                    flood[r][c] = 0
                    water.append((r, c))
                elif land[r][c] == "S":
                    start = (r, c)

        def neighbors(r: int, c: int):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < m and 0 <= cc < n:
                    yield rr, cc

        while water:
            r, c = water.popleft()
            for rr, cc in neighbors(r, c):
                if land[rr][cc] in ".S" and flood[rr][cc] > flood[r][c] + 1:
                    flood[rr][cc] = flood[r][c] + 1
                    water.append((rr, cc))
        queue = deque([(start[0], start[1], 0)])
        visited = {start}
        while queue:
            r, c, t = queue.popleft()
            if land[r][c] == "D":
                return t
            for rr, cc in neighbors(r, c):
                if (
                    land[rr][cc] != "X"
                    and (rr, cc) not in visited
                    and t + 1 < flood[rr][cc]
                ):
                    visited.add((rr, cc))
                    queue.append((rr, cc, t + 1))
        return -1
