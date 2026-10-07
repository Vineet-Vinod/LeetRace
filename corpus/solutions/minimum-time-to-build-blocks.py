from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heap = blocks[:]
        heapify(heap)
        while len(heap) > 1:
            heappop(heap)
            larger = heappop(heap)
            heappush(heap, larger + split)
        return heap[0]
