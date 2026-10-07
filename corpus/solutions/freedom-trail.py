from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        positions = defaultdict(list)
        for i, char in enumerate(ring):
            positions[char].append(i)
        dp = {0: 0}
        n = len(ring)
        for char in key:
            dp = {
                j: min(
                    cost + min(abs(i - j), n - abs(i - j)) + 1 for i, cost in dp.items()
                )
                for j in positions[char]
            }
        return min(dp.values())
