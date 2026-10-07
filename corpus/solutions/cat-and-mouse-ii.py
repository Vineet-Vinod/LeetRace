from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        from collections import deque

        cells = [
            (r, c)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value != "#"
        ]
        indices = {cell: i for i, cell in enumerate(cells)}
        start_mouse = next(i for i, (r, c) in enumerate(cells) if grid[r][c] == "M")
        start_cat = next(i for i, (r, c) in enumerate(cells) if grid[r][c] == "C")
        food = next(i for i, (r, c) in enumerate(cells) if grid[r][c] == "F")

        def moves(jump):
            result = []
            for r, c in cells:
                options = [indices[(r, c)]]
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    for length in range(1, jump + 1):
                        point = (r + dr * length, c + dc * length)
                        if point not in indices:
                            break
                        options.append(indices[point])
                result.append(options)
            return result

        mouse_moves, cat_moves = moves(mouseJump), moves(catJump)
        size = len(cells)
        # The attractor ranks count individual moves; unresolved states let Cat delay forever.
        rank = [[[-1, -1] for _ in cells] for _ in cells]
        remaining = [[len(cat_moves[c]) for c in range(size)] for _ in cells]
        longest = [[0] * size for _ in cells]
        queue = deque()
        for c in range(size):
            if c != food:
                for turn in (0, 1):
                    rank[food][c][turn] = 0
                    queue.append((food, c, turn))
        while queue:
            m, c, turn = queue.popleft()
            distance = rank[m][c][turn]
            if turn == 1:
                for previous in mouse_moves[m]:
                    if (
                        previous == c
                        or c == food
                        or previous == food
                        or rank[previous][c][0] >= 0
                    ):
                        continue
                    rank[previous][c][0] = distance + 1
                    queue.append((previous, c, 0))
            else:
                for previous in cat_moves[c]:
                    if (
                        previous == m
                        or previous == food
                        or m == food
                        or rank[m][previous][1] >= 0
                    ):
                        continue
                    remaining[m][previous] -= 1
                    longest[m][previous] = max(longest[m][previous], distance + 1)
                    if remaining[m][previous] == 0:
                        rank[m][previous][1] = longest[m][previous]
                        queue.append((m, previous, 1))
        return 0 <= rank[start_mouse][start_cat][0] <= 1000
