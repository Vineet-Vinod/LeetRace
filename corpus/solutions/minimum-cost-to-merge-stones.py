from typing import List
from functools import lru_cache


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        @lru_cache(None)
        def cost(i, j):
            if j - i + 1 < k:
                return 0
            answer = min(cost(i, m) + cost(m + 1, j) for m in range(i, j, k - 1))
            if (j - i) % (k - 1) == 0:
                answer += prefix[j + 1] - prefix[i]
            return answer

        return cost(0, n - 1)
