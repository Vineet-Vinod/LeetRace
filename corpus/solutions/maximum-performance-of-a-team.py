from typing import List
from heapq import heappush, heappop


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        heap = []
        total = best = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(heap, s)
            total += s
            if len(heap) > k:
                total -= heappop(heap)
            best = max(best, total * e)
        return best % 1000000007
