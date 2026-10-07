class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        return all(
            abs(x - target[0]) + abs(y - target[1]) > distance for x, y in ghosts
        )
