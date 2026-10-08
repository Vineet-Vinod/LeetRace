class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prices: list[int] = []
        beauties: list[int] = []
        best = 0
        for price, beauty in items:
            best = max(best, beauty)
            if prices and prices[-1] == price:
                beauties[-1] = best
            else:
                prices.append(price)
                beauties.append(best)
        return [
            beauties[bisect_right(prices, query) - 1]
            if bisect_right(prices, query)
            else 0
            for query in queries
        ]
