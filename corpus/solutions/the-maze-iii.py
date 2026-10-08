from heapq import heappop, heappush


class Solution:
    def findShortestWay(
        self, maze: list[list[int]], ball: list[int], hole: list[int]
    ) -> str:
        m, n = len(maze), len(maze[0])
        best = {tuple(ball): (0, "")}
        queue = [(0, "", ball[0], ball[1])]
        while queue:
            distance, path, i, j = heappop(queue)
            if best.get((i, j)) != (distance, path):
                continue
            if [i, j] == hole:
                return path
            for di, dj, letter in (
                (1, 0, "d"),
                (0, -1, "l"),
                (0, 1, "r"),
                (-1, 0, "u"),
            ):
                x, y, steps = i, j, 0
                while 0 <= x + di < m and 0 <= y + dj < n and maze[x + di][y + dj] == 0:
                    x += di
                    y += dj
                    steps += 1
                    if [x, y] == hole:
                        break
                if not steps:
                    continue
                current = (distance + steps, path + letter)
                if (x, y) not in best or current < best[x, y]:
                    best[x, y] = current
                    heappush(queue, (*current, x, y))
        return "impossible"
