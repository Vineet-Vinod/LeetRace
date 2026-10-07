class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        inf = 10**18
        prices = [inf] * n
        prices[src] = 0
        for _ in range(k + 1):
            updated = prices.copy()
            for start, end, cost in flights:
                if prices[start] != inf:
                    updated[end] = min(updated[end], prices[start] + cost)
            prices = updated
        return -1 if prices[dst] == inf else prices[dst]
