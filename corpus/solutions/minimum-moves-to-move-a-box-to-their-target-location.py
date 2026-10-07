from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        from collections import deque

        rows, cols = len(grid), len(grid[0])
        floor = {(i, j) for i in range(rows) for j in range(cols) if grid[i][j] != "#"}
        positions = {grid[i][j]: (i, j) for i, j in floor if grid[i][j] in "SBT"}
        start, box, target = positions["S"], positions["B"], positions["T"]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(box, start, 0)])
        seen = {(box, start)}
        while queue:
            current, player, pushes = queue.popleft()
            if current == target:
                return pushes
            reachable = {player}
            walk = [player]
            for x, y in walk:
                for dx, dy in directions:
                    following = (x + dx, y + dy)
                    if (
                        following in floor
                        and following != current
                        and following not in reachable
                    ):
                        reachable.add(following)
                        walk.append(following)
            x, y = current
            for dx, dy in directions:
                following = (x + dx, y + dy)
                behind = (x - dx, y - dy)
                state = (following, current)
                if behind in reachable and following in floor and state not in seen:
                    seen.add(state)
                    queue.append((following, current, pushes + 1))
        return -1
