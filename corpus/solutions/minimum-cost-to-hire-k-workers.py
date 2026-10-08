from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        from heapq import heappush, heappop

        heap: list[int] = []
        total = 0
        answer = float("inf")
        for ratio, q in sorted((w / q, q) for q, w in zip(quality, wage)):
            total += q
            heappush(heap, -q)
            if len(heap) > k:
                total += heappop(heap)
            if len(heap) == k:
                answer = min(answer, ratio * total)
        return answer
