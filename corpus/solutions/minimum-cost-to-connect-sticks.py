class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks[:]
        heapify(heap)
        cost = 0
        while len(heap) > 1:
            combined = heappop(heap) + heappop(heap)
            cost += combined
            heappush(heap, combined)
        return cost
