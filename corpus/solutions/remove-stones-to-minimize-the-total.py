class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapify(heap)
        for _ in range(k):
            pile = -heappop(heap)
            heappush(heap, -(pile - pile // 2))
        return -sum(heap)
