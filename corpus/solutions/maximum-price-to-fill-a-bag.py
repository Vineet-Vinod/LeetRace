class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        remaining = capacity
        total_price = 0.0
        for price, weight in sorted(
            items, key=lambda item: item[0] / item[1], reverse=True
        ):
            if remaining == 0:
                return total_price
            used = min(remaining, weight)
            total_price += used * price / weight
            remaining -= used
        return total_price if remaining == 0 else -1.0
