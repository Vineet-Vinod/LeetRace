from typing import List
import heapq


class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def increasing(values):
            heap = []
            cost = 0
            for value in values:
                heapq.heappush(heap, -value)
                if -heap[0] > value:
                    cost += -heapq.heappop(heap) - value
                    heapq.heappush(heap, -value)
            return cost

        return min(increasing(nums), increasing(nums[::-1]))
