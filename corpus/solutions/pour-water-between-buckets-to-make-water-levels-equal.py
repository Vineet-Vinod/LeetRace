class Solution:
    def equalizeWater(self, buckets: list[int], loss: int) -> float:
        low, high = 0.0, float(max(buckets))
        efficiency = 100 - loss
        for _ in range(60):
            level = (low + high) / 2
            available = sum(max(0.0, amount - level) * efficiency for amount in buckets)
            needed = sum(max(0.0, level - amount) * 100 for amount in buckets)
            if available >= needed:
                low = level
            else:
                high = level
        return round(low, 5)
