from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        grid = [row[:] for row in isInfected]
        m, n = len(grid), len(grid[0])
        answer = 0
        while True:
            seen = set()
            regions = []
            for r in range(m):
                for c in range(n):
                    if grid[r][c] != 1 or (r, c) in seen:
                        continue
                    cells, frontier, walls = [], set(), 0
                    todo = [(r, c)]
                    seen.add((r, c))
                    while todo:
                        x, y = todo.pop()
                        cells.append((x, y))
                        for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                            if not (0 <= a < m and 0 <= b < n):
                                continue
                            if grid[a][b] == 0:
                                frontier.add((a, b))
                                walls += 1
                            elif grid[a][b] == 1 and (a, b) not in seen:
                                seen.add((a, b))
                                todo.append((a, b))
                    regions.append((cells, frontier, walls))
            if not regions or max(len(reg[1]) for reg in regions) == 0:
                return answer
            chosen = max(range(len(regions)), key=lambda i: len(regions[i][1]))
            answer += regions[chosen][2]
            for i, (cells, frontier, _) in enumerate(regions):
                if i == chosen:
                    for r, c in cells:
                        grid[r][c] = -1
                else:
                    for r, c in frontier:
                        grid[r][c] = 1
