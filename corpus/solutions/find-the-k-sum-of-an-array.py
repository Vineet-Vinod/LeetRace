from heapq import heappush, heappop


class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        total = sum(x for x in nums if x > 0)
        if k == 1:
            return total
        a = sorted(abs(x) for x in nums)
        heap = [(a[0], 0)]
        value = 0
        for _ in range(k - 1):
            value, i = heappop(heap)
            if i + 1 < len(a):
                heappush(heap, (value + a[i + 1], i + 1))
                heappush(heap, (value - a[i] + a[i + 1], i + 1))
        return total - value
