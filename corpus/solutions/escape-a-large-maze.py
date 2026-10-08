from typing import List
from collections import deque


class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        walls = {tuple(cell) for cell in blocked}
        bound = len(walls) * (len(walls) - 1) // 2

        def escapes(start: List[int], goal: List[int]) -> bool:
            seen = {tuple(start)}
            queue = deque([tuple(start)])
            while queue and len(seen) <= bound:
                x, y = queue.popleft()
                if (x, y) == tuple(goal):
                    return True
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (
                        0 <= nx < 10**6
                        and 0 <= ny < 10**6
                        and (nx, ny) not in walls
                        and (nx, ny) not in seen
                    ):
                        seen.add((nx, ny))
                        queue.append((nx, ny))
            return len(seen) > bound

        return escapes(source, target) and escapes(target, source)
