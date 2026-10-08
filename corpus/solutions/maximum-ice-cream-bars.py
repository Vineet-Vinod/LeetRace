class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        frequencies = [0] * 100_001
        for cost in costs:
            frequencies[cost] += 1
        bought = 0
        for cost, count in enumerate(frequencies):
            take = min(count, coins // cost) if cost else count
            bought += take
            coins -= take * cost
            if coins == 0:
                break
        return bought
