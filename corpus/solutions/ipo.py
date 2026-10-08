from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        projects = sorted(zip(capital, profits))
        index = 0
        heap = []
        for _ in range(min(k, len(profits))):
            while index < len(projects) and projects[index][0] <= w:
                heappush(heap, -projects[index][1])
                index += 1
            if not heap:
                break
            w -= heappop(heap)
        return w
