class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        possible = set(baseCosts)
        for topping in toppingCosts:
            next_possible = set()
            for cost in possible:
                next_possible.add(cost)
                next_possible.add(cost + topping)
                next_possible.add(cost + 2 * topping)
            possible = next_possible
        return min(possible, key=lambda cost: (abs(cost - target), cost))
