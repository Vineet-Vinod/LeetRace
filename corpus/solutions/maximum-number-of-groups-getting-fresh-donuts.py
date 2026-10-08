from typing import List


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        from functools import lru_cache

        counts = [0] * batchSize
        for group in groups:
            counts[group % batchSize] += 1
        happy = counts[0]
        counts[0] = 0
        for remainder in range(1, (batchSize + 1) // 2):
            pairs = min(counts[remainder], counts[batchSize - remainder])
            happy += pairs
            counts[remainder] -= pairs
            counts[batchSize - remainder] -= pairs
        if batchSize % 2 == 0:
            happy += counts[batchSize // 2] // 2
            counts[batchSize // 2] %= 2
        initial_sum = sum(i * count for i, count in enumerate(counts))

        @lru_cache(None)
        def search(state):
            current = (
                initial_sum - sum(i * count for i, count in enumerate(state))
            ) % batchSize
            best = 0
            for remainder in range(1, batchSize):
                if state[remainder]:
                    following = list(state)
                    following[remainder] -= 1
                    best = max(best, (current == 0) + search(tuple(following)))
            return best

        return happy + search(tuple(counts))
