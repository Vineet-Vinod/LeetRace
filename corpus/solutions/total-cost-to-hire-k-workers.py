class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = 0
        right = n - 1
        heap = []
        for _ in range(candidates):
            if left <= right:
                heappush(heap, (costs[left], left))
                left += 1
        for _ in range(candidates):
            if left <= right:
                heappush(heap, (costs[right], right))
                right -= 1
        total = 0
        for _ in range(k):
            cost, index = heappop(heap)
            total += cost
            if left <= right:
                if index < left:
                    heappush(heap, (costs[left], left))
                    left += 1
                else:
                    heappush(heap, (costs[right], right))
                    right -= 1
        return total
