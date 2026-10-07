class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        first, second = Counter(basket1), Counter(basket2)
        excess = []
        for value in first.keys() | second.keys():
            difference = first[value] - second[value]
            if difference % 2:
                return -1
            excess.extend([value] * (abs(difference) // 2))
        excess.sort()
        cheapest = min(min(basket1), min(basket2))
        return sum(min(value, 2 * cheapest) for value in excess[: len(excess) // 2])
