from heapq import heapify, heappop, heappush


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(heap)
        maximum = max(row[0] for row in nums)
        best = [heap[0][0], maximum]
        while True:
            minimum, row, index = heappop(heap)
            if (maximum - minimum, minimum) < (best[1] - best[0], best[0]):
                best = [minimum, maximum]
            index += 1
            if index == len(nums[row]):
                return best
            value = nums[row][index]
            maximum = max(maximum, value)
            heappush(heap, (value, row, index))
