class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums[:]
        heapify(heap)
        operations = 0
        while heap[0] < k:
            first = heappop(heap)
            second = heappop(heap)
            heappush(heap, first * 2 + second)
            operations += 1
        return operations
