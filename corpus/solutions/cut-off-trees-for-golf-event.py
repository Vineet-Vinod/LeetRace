from collections import deque


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        rows, cols = len(forest), len(forest[0])
        trees = sorted(
            (forest[r][c], r, c)
            for r in range(rows)
            for c in range(cols)
            if forest[r][c] > 1
        )
        if forest[0][0] == 0:
            return -1
        current = (0, 0)
        total = 0
        for _, target_r, target_c in trees:
            target = (target_r, target_c)
            queue = deque([(current[0], current[1], 0)])
            seen = {current}
            found = -1
            while queue:
                r, c, distance = queue.popleft()
                if (r, c) == target:
                    found = distance
                    break
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and forest[nr][nc]
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc, distance + 1))
            if found < 0:
                return -1
            total += found
            current = target
        return total
