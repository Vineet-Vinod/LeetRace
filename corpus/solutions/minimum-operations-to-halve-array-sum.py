class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-float(value) for value in nums]
        heapify(heap)
        target_reduction = sum(nums) / 2
        reduction = 0.0
        operations = 0
        while reduction < target_reduction:
            value = -heappop(heap)
            half = value / 2
            reduction += half
            heappush(heap, -half)
            operations += 1
        return operations
