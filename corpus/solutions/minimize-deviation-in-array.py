from heapq import heapify, heappop, heappush


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        normalized = [x * 2 if x % 2 else x for x in nums]
        low = min(normalized)
        heap = [-x for x in normalized]
        heapify(heap)
        answer = -heap[0] - low
        while True:
            high = -heappop(heap)
            answer = min(answer, high - low)
            if high % 2:
                return answer
            high //= 2
            low = min(low, high)
            heappush(heap, -high)
