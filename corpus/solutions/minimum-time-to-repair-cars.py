class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 0, min(ranks) * cars * cars
        while low < high:
            middle = (low + high) // 2
            repaired = sum(math.isqrt(middle // rank) for rank in ranks)
            if repaired >= cars:
                high = middle
            else:
                low = middle + 1
        return low
