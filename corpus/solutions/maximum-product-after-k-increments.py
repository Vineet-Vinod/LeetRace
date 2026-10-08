from heapq import heapify, heappop, heappush


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap = nums[:]
        heapify(heap)
        for _ in range(k):
            smallest = heappop(heap)
            heappush(heap, smallest + 1)
        product = 1
        for value in heap:
            product = product * value % (10**9 + 7)
        return product
