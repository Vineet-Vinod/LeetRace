class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq

        heap = [-x for x in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            largest = -heapq.heappop(heap)
            heapq.heappush(heap, -math.isqrt(largest))
        return -sum(heap)
