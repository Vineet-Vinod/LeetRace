class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)
        while len(heap) > 1:
            first, second = -heappop(heap), -heappop(heap)
            if first != second:
                heappush(heap, -(first - second))
        return -heap[0] if heap else 0
