from typing import List
from collections import deque


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        queue = deque([(n + 1, 0)])
        result = 0
        for i in range(n, 0, -1):
            while queue[0][0] > 2 * i + 1:
                queue.popleft()
            result = prices[i - 1] + queue[0][1]
            while queue and queue[-1][1] >= result:
                queue.pop()
            queue.append((i, result))
        return result
