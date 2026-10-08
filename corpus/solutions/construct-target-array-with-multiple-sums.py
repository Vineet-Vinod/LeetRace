from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        import heapq

        heap = [-value for value in target]
        heapq.heapify(heap)
        total = sum(target)
        while -heap[0] > 1:
            largest = -heapq.heappop(heap)
            rest = total - largest
            if rest == 1:
                return True
            if rest == 0 or rest >= largest:
                return False
            previous = largest % rest
            if previous == 0:
                return False
            total = rest + previous
            heapq.heappush(heap, -previous)
        return True
